from . import get
from . import process


def search(keyword, **kwargs):
    #使用setdefault函数设置一个字典，其中key='convey',value=False
    kwargs.setdefault('convey', False)
    #调用自定义的get函数，传入想要搜索的关键字，get返回搜索结果的页面
    page = get.page(keyword)
    #调用自定义的process函数，解析页面，返回每一条搜索的结果
    results = process.page(page)
    if kwargs['convey']:
        for result in results:
            result.convey_url()
    return results
