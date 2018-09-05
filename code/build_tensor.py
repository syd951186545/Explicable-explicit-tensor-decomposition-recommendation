# _*_ coding:utf-8 _*_
__AUTHOR__ = "syd"
# DATA:2018/9/5
# PROJECT:Pyworkplace

import numpy as np
import tensorly as tl
import tensorflow as tf
from scipy import sparse as sp


class Build_tensor:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.num_users = 0
        self.num_items = 0
        self.num_features = 0
        self.num_datas = 0
        self.pieces = []

    def load_data(self):
        """
        读取文件，获得用户，产品，特征的总数，并且得到规范化的数据
        :return:
        """
        with open(self.infile, "r") as infile:
            for line in infile.readlines():
                feature_list = []
                line = line.split(",")
                line[3] = line[3].replace("\n", "")
                for featureS in line[3].split(" "):
                    templist = featureS.split(":")
                    feature_list.append((int(templist[0]), int(templist[1])))
                    if self.num_features < int(templist[0]):
                        self.num_features = int(templist[0])
                if self.num_users < int(line[0]):
                    self.num_users = int(line[0])
                if self.num_items < int(line[1]):
                    self.num_items = int(line[1])
                self.pieces.append([int(line[0]), int(line[1]), int(line[2]), feature_list])
                self.num_datas += 1
                print(self.num_datas)

    def build_tensor(self):
        self.load_data()
        TsnsorX = np.ndarray(shape=(self.num_users,self.num_items,self.num_features),dtype=np.float16)
        # TsnsorX = tl.zeros(shape=(self.num_users,self.num_items,self.num_features))
        # TsnsorX = tf.SparseTensor()
        # TsnsorX = sp.coo_matrix(shape=(self.num_users,self.num_items,self.num_features))
        for piece in self.pieces:
            for feature in piece[3]:
                # indices = [piece[0], piece[1], featur[0]]
                # values +=
                # TsnsorX = tf.SparseTensor(indices=indices, values=featur[1])
                TsnsorX[piece[0]][piece[1]][feature[0]] += np.float(feature[1])
        TsnsorX = tl.tensor(TsnsorX)
        return TsnsorX
    def build_others(self):
        return


if __name__ == "__main__":
    bt = Build_tensor(infile="E:\ALLworkspace\Pyworkplace\TensorDecomposition\datas\\test.entry",
                      outfile="E:\ALLworkspace\Pyworkplace\TensorDecomposition\\result\\UFO.sparsemat")
    print(bt.build_tensor())
