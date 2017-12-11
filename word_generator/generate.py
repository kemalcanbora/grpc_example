import pandas as pd
from gensim import models
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from pprint import pprint
import logging
import os.path
import sys
import multiprocessing



def create_model(input_path):

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))



    inp= input_path##/home/kb/Belgeler/gundem-nz.txt
    outp="tt.tr.word2vec.model"

    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count()) ##LineSentence(inp)

    ## trim unneeded model memory = use (much) less RAM
    model.init_sims(replace=True)

    model.save(outp)

def calistir(sorgu):

    model = models.Word2Vec.load("tt.tr.word2vec.model")

    sonuc=model.most_similar(sorgu,topn=5)
    pprint(sonuc)


create_model("/home/kb/Belgeler/glove.840B.300d.txt")
calistir(sorgu= ['frog'] )
