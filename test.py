from embedgen.component.parser import DocParser

if __name__ == '__main__':
    p = DocParser("artifacts\input\download.jpg")
    p.getOcrPrediction()