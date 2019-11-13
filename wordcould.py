from wordcloud import WordCloud
# import wordcloud
text_file = open('wakati_list.txt', encoding='utf-8')
f = text_file.read()

fpath = '/System/Library/Fonts/ヒラギノ角ゴシック W0.ttc'


#無意味そうな単語除去
stop_words = ['そう', 'ない', 'いる', 'する', 'まま', 'よう', 'てる', 'なる', 'こと', 'もう', 'いい', 'ある', 'ゆく', 'れる', 'そこ', 'ここ', 'くる', 'ぼる', 'どこ', 'ちる', 'くれる', 'いく', 'やる', 'どう', 'られる', 'りん', 'もらう', 'それ', 'よく', '見る', '会う', '来る', '行く', '居る', '望む']

wordcloud = WordCloud(background_color='white', font_path=fpath, width=800, height=600, stopwords=set(stop_words)).generate(f)

wordcloud.to_file('./wordcloud.png')