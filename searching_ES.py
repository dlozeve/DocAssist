import datetime
import logging
import os
import time

from elasticsearch import Elasticsearch

from elasticsearch_dsl import Search, Q

from config import config_path


class SearchES(config_path):
    def __init__(self, n_results):
        config_path.__init__(self)

        self.n_results = n_results

        self.dt = datetime.datetime.now()
        self.start_time = time.time()

        self.log_file_name = os.path.join(self.logs_dir,
                                          "searching_%s%s%s_%s_%s" % (self.dt.year, self.dt.month, self.dt.day,
                                                                      self.dt.hour, self.dt.minute))
        logging.basicConfig(filename=self.log_file_name,
                            level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt='%Y/%m/%d %H:%M:%S')

    def Search(self):

        es = Elasticsearch([{'host': self.host, 'port': self.port}])

        D0 = open(self.transcript_D2, 'r').read()
        # search_H = open(self.transcript_H, 'r').read()
        # search_E = open(self.transcript_E, 'r').read()
        # search_T = open(self.transcript_T, 'r').read()

        # query = D0 + ' ' + search_H + ' ' + search_E + ' ' + search_T
        query=D0

        fields = ['title']

        q = Q("multi_match", query=query, fields=fields)

        s = Search(using=es, index=self.index).query(q)[:self.n_results]
        response = s.execute()

        n_hits = response.hits.total

        logging.info("\n=========================================================================================")
        logging.info("host: %s \t port: %s \t index: %s \t doc_type: %s" % (self.host, self.port,
                                                                            self.index, self.doc_type))
        logging.info("Nb of hits: %s" % n_hits)
        logging.info("Running time: %0.2f seconds" % (time.time() - self.start_time))

        if n_hits == 0:
            return('no results;')
        else:
            Ll = []
            for j in range(min(n_hits,self.n_results)):
                Ll.append(str(j) + '. ' + response.hits[j].title + ', ' + response.hits[j].doi )

            return("\n".join(Ll) + ';')



# print(SearchES(n_results=5).Search())