
# python code type
import tkinter as tk
window = tk.Tk()
window.title('compensation rate finder')
window.geometry('400x450')

head = tk.Label(window,
    text='補助費率計算機',    # 标签的文字
    #bg='white',     # 背景颜色
    font=('Arial', 14),     # 字体和字体大小
    width=10, height=2  # 标签长宽
    )
head.pack()    # 固定窗口位置
#標籤收支比
inoutratio_L = tk.Label(window,
    text='收支比',
    font=('Arial', 13),
    width=8, height=2
    )
inoutratio_L.place(x = 10, y = 50)

tk.Label(window, text='收入金額: ').place(x=15, y= 100)
tk.Label(window, text='總人口: ').place(x=15, y= 140)

#計算收支比
#收支比
#收
#A
A = tk.IntVar(value=1)
#entry_incomeA = tk.Entry(window,textvariable=A, width=5 ) #textvariable設定entry裡面是數字>>>錯誤用法
entry_incomeA = tk.Entry(window, textvariable=A, width=5 )
entry_incomeA.place(x=80, y= 100)
 #.get()得到文字
#B
B = tk.IntVar(value=1)
#entry_incomeB = tk.Entry(window,textvariable=B, width=5 )
entry_incomeB = tk.Entry(window, textvariable=B, width=5 )
entry_incomeB.place(x=130, y= 100)

#C
C= tk.IntVar()
entry_incomeC = tk.Entry(window, textvariable=C, width=5 )
entry_incomeC.place(x=180, y= 100)

#D
D= tk.IntVar()
entry_incomeD = tk.Entry(window, textvariable=D, width=5 )
entry_incomeD.place(x=230, y= 100)

#E
E= tk.IntVar()
entry_incomeE = tk.Entry(window, textvariable=E, width=5 )
entry_incomeE.place(x=280, y= 100)

#支
taipei_spent = 15544
spent = tk.IntVar(value=1)  #把預設設定為1
entry_spent_population = tk.Entry(window, textvariable=spent, width=4 )
entry_spent_population.place(x=80, y= 140)
#spent_population = int(entry_spent_population.get())
#income_spent_ratio = incomeA + incomeB + incomeC + incomeD + incomeE/spent_population * taipei_spent
# 工作比

inoutratio_L = tk.Label(window,
    text='工作比',
    font=('Arial', 13),
    width=8, height=2
    )
inoutratio_L.place(x = 10, y = 190)

tk.Label(window, text='工作人口數: ').place(x=15, y= 230)
tk.Label(window, text='總人口數: ').place(x=15, y= 270)
#工作比空格
#工作人口
work = tk.IntVar(value=1)
entry_working_population= tk.Entry(window, textvariable=work, width=4 )
entry_working_population.place(x= 84, y = 230)
#working_population = int(entry_working_population.get())  先在entry 轉成數字不知道為什麼無法運算
#總人口數
nonwork = tk.IntVar(value=1)
entry_allpopulation= tk.Entry(window, textvariable=nonwork, width=4 )
entry_allpopulation.place(x= 84, y = 270)
#allpopulation = int(entry_allpopulation.get())
#working_ratio = working_population/ allpopulation

def insert_data():
    #income_spent_ratio = (incomeA + incomeB + incomeC + incomeD + incomeE)/spent_population * taipei_spent
    iA = int(str(entry_incomeA.get()))
    iB = int(str(entry_incomeB.get()))
    iC = int(str(entry_incomeC.get()))
    iD = int(str(entry_incomeD.get()))
    iE = int(str(entry_incomeE.get()))

    sP = int(str(entry_spent_population.get()))

    #working_ratio_formula
    var1 = int(((iA+iB+iC+iD+iE)/(sP*taipei_spent))*100)

    #working_ratio = working_population/ allpopulation
    wP = int(str(entry_working_population.get()))
    allP = int(str(entry_allpopulation.get()))
    var2 = int((wP/allP)*100)

    var = var1 * var2
    #k.insert('insert', var)

    return (var)


def cal():
    a3 = int(insert_data())
    y = 15
    x = 10
    z = 50
    for i in range(10):
        if a3 <= x * y :
            return(z)
            break
        else:
            y = y + 15
            x = x + 10
            z = z - 5

k = tk.Text(window, width=4, height=2,)
k.place(x=300, y=380)
def call_data():
    e = cal()
    #return (e)
    k.insert('insert',e)

#button1 = tk.Button(window,text="計算", width=8,height=2,command=insert_data)
#button1.place(x= 100, y=320)

b2 = tk.Button(window,text="計算", width=8,height=2,
                   command=call_data)
b2.place(x= 100, y=350)

#show_result = tk.Label(window, width=4, height=2, text=cal())
#show_result.place(x=300, y=320)



window.mainloop()
