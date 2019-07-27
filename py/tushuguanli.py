def status_str(status):
    if status:
        return "已借出"
    return "未借出"


class Book:
    def __init__(self, title, author="", recommendation="", status=False):
        self.title = title
        self.author = author
        self.recommendation = recommendation
        self.status = status

    def __str__(self):
        return "名称：《{}》 作者：{} 推荐语：{}\n状态：{} ".format(
            self.title, self.author, self.recommendation, status_str(self.status))


class BookManager:
    books = []

    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿',
                     '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book(
            '以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯',
                     '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海中相遇。')
                break

    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        name = input('请输入书籍名称：')
        author = input("请输入作者名字：")
        recom = input("请输入推荐语：")
        self.books.append(Book(name, author, recom))
        print("{0:*^20}".format("已添加书籍"))
        print(self.books[-1])
        print("{0:*^20}".format(""))

    def __check_book(self, name):
        for book in self.books:
            if book.title == name:
                return book
        return None

    def lend_book(self):
        name = input('请输入借阅书籍的名称：')
        res = self.__check_book(name)

        if res != None:
            if res.status == True:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.status = False
        else:
            print('这本书暂时没有收录在系统里呢')

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.__check_book(name)
        if res != None:
            print('读的很快哦')
            res.status = False
        else:
            print('这本书没有收录在系统里呢')

manager = BookManager()
manager.menu()
