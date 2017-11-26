import datetime
import logging
import os
import time

import pandas as pd
from elasticsearch import Elasticsearch

from config import config_path


class IndexES(config_path):
    def __init__(self, delete_index):
        config_path.__init__(self)

        self.delete_index = delete_index

        self.dt = datetime.datetime.now()
        self.start_time = time.time()

        self.log_file_name = os.path.join(self.logs_dir,
                                          "indexing_%s%s%s_%s_%s" % (self.dt.year, self.dt.month, self.dt.day,
                                                                      self.dt.hour, self.dt.minute))

    def indexit(self):

        logging.basicConfig(filename=self.log_file_name,
                            level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt='%Y/%m/%d %H:%M:%S')

        es = Elasticsearch([{'host': self.host, 'port': self.port}])

        if self.delete_index:
            es.indices.delete(index=self.index, ignore=[400, 404])
            print("index %s deleted" % self.index)

        ref = pd.read_csv(self.research_papers,
                          header=0,
                          sep=',',
                          encoding='utf8')
        print('data loaded')

        for i in range(0, len(ref)):
            doc = {
                "title": str(ref.title[i]),
                "descriptor_name": str(ref.descriptor_name[i]),
                "doi": str(ref.doi[i]),
                "year": str(ref.year[i]),
                "journal_title": str(ref.doi[i])
            }

            _ = es.index(index=self.index, doc_type=self.doc_type, id=i, body=doc)

            if (i % 50 == 0) & (i != 0):
                print("%s/%s" % (i, len(ref)))

            logging.info("\n=========================================================================================")
            logging.info("host: %s \t port: %s \t index: %s \t doc_type: %s" % (self.host, self.port,
                                                                                self.index, self.doc_type))
            logging.info("Data indexed: %s" % os.path.basename(os.path.normpath(self.research_papers)))
            logging.info("n_lines indexed: %s" % (len(ref)))
            logging.info("Running time: %0.3f seconds" % (time.time() - self.start_time))
            logging.info("-- by line: %0.6f seconds" % ((time.time() - self.start_time) / (len(ref))))

if __name__ == '__main__':
    idx = IndexES(delete_index=True)
    idx.indexit()