from bs4 import BeautifulSoup
import unittest
import re
import os

def parse(path_to_file):
    import re
    def open_file(file):
        with open(file, encoding='utf-8') as f:
            return f.read()

    file = open_file(path_to_file)
    soup = BeautifulSoup(file, 'lxml')
    body = soup.find('div', id="bodyContent")
    imgs, headers, linkslen, lists = [0, 0, 0, 0]
    img = body('img')
    for im in img:
        if im.attrs.get('width'):
            if int(im.attrs.get('width')) >= 200:
                imgs +=1

    hea = body.find_all(name = re.compile('^h[123456]'))
    for tx in hea:
        if tx.text:
            if tx.text[0] == 'E' or tx.text[0] == 'T' or tx.text[0] == 'C':
                headers +=1

    link = body("a")

    def find_a(tag, count=1):


        if tag.find_next_sibling():
            #print(tag.find_next_sibling().name)
            if tag.find_next_sibling().name == 'a':
                return find_a(tag.find_next_sibling(), count +1)
            else:
                return count
        else:
            return count

    for li in link:
        c = find_a(li)
        if c > linkslen:
            linkslen = c

    lists_ol = body("ol")
    list_ul = body("ul")
    for item in lists_ol:
        if item.find_parent("ol"):
            continue
        if item.find_parent("ul"):
            continue
        lists +=1
    for item in list_ul:
        if item.find_parent("ol"):
            continue
        if item.find_parent("ul"):
            continue
        lists += 1
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


def build_bridge(path, start_page, end_page):
    def open_page(path, page):
        with open(os.path.join(path, page), encoding = "utf-8") as file:
            links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
            list_ref = set()
            for f in links:
                if os.path.exists(f) and f != page:
                    list_ref.add(f)
            return list_ref
a = open_page(path, start_page)



    links = open_page(path, start_page)



    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    # напишите вашу реализацию логики по вычисления кратчайшего пути здесь


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь

    return statistic



if __name__ == '__main__':
    unittest.main()