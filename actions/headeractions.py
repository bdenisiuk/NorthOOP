from pages.articlepage import ArticlePage
from pages.grouppage import GroupPage
from pages.searchpage import SearchPage

class HeaderActions:


    def __init__(self):
        self.driver = None

    def check_search_result(self, url):
        print('Function redirecting searched phrase')
        if "/karta/" in url:
            print(f'Redirected to article page {url}')
            return ArticlePage(self.driver)
        
        if ",g" in url:
            print(f'Redirected to group page {url}')
            return GroupPage(self.driver)

        elif "/s/" in url:
            print(f'Redirected to search page {url}')
            return SearchPage(self.driver)
        else:
            # TODO obsluzenie wyjatku
            pass



        # grupa