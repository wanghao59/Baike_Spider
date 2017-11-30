# coding:utf-8
# html输出展示器

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 输出格式问题，python3 需要在open函数里面直接指定编码格式为 utf-8
        # Python2的写法
        # fout = open('output.html', 'w')

        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<meta charset=\'utf-8\'>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            print(data)
            fout.write('<tr>')
            # fout.write('<td>%s</td>' % data['url'])

            # python2的写法
            # fout.write('<td><a href="%s">%s</a></td>' % (data['url'],data['title']))
            # fout.write('<td>%s</td>' % data['summary'])

            fout.write('<td><a href="%s">%s</a></td>' % (data['url'],data['title']))
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')