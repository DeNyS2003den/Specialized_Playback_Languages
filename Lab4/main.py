from CustomArt import CustomArt

font = {
    'm': '1',
    'e':'2',
    's':'3'
}
art = CustomArt('hp')

# art._size_x = 10
# art._size_y = 12
# art.zoom()
# print(art.prev_view())
#
art.justify = 'right'
art.create()
print(art)

art.justify = 'center'
art.create()
print(art)


art.justify = 'left'
art.create()
print(art)


