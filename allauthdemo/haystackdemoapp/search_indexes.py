import datetime
from haystack import indexes
from haystackdemoapp.models import Note

# 只对部分字段建立索引  存到ES索引库去了

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # 就是当模型类中的索引有更新时进行调用
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())