map_values= [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
row = input( "enter the row value")
column = input( "enter the column value")
map_values[int(row)-1][int(column)-1] ='x'
print(map_values)