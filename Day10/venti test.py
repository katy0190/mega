import venti

# 엑셀 #데이터베이스
selling_menu_items = []

a = venti.coffee('아이스 아메리카노', '/iceAmericano', True, False)
b = venti.coffee('라떼', '/latte', True, True)
c = venti.Juice('체리콕', '/cherryCoke')

selling_menu_items.append(a)
selling_menu_items.append(b)
selling_menu_items.append(c)

