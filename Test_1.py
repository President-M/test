import tkinter as tk

# 创建GUI界面
root = tk.Tk()
root.title("赛事评分系统")

# 定义打分表头
table_headers = ["参赛人员", "得分", "评委1", "评委2", "评委3", "评委4", "评委5"]

# 添加标题和图片
title_label = tk.Label(root, text="赛事评分系统", font=("Arial", 20, "bold"), pady=10)
title_label.pack()

img = tk.PhotoImage(file="/Users/chengming/Desktop/v2-8fc862a5f90a74540a3f4f39e034f864_b.gif")
img_label = tk.Label(root, image=img, pady=10)
img_label.pack()

# 添加参赛人员列表
contestants_listbox = tk.Listbox(root, height=10)
contestants_listbox.pack(side=tk.LEFT, padx=5, pady=5)

# 添加评委列表
judges_listbox = tk.Listbox(root, height=10)
judges_listbox.pack(side=tk.LEFT, padx=5, pady=5)

# 添加打分表格
table_frame = tk.Frame(root)
table_frame.pack(side=tk.LEFT, padx=5, pady=5)

# 添加表头
for i, header in enumerate(table_headers):
    header_label = tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), padx=10, pady=5)
    header_label.grid(row=0, column=i)

# 添加表格数据
for i in range(1, 3):
    # 添加参赛人员名称
    contestant_label = tk.Label(table_frame, text="参赛人员" + str(i), font=("Arial", 12))
    contestant_label.grid(row=i, column=0)

    # 添加得分框
    score_entry = tk.Entry(table_frame, font=("Arial", 12), width=8)
    score_entry.grid(row=i, column=1)

    # 添加评委打分框
    for j in range(2, 7):
        score_entry = tk.Entry(table_frame, font=("Arial", 12), width=8)
        score_entry.grid(row=i, column=j)

# 添加总得分按钮
total_score_button = tk.Button(table_frame, text="计算总得分", font=("Arial", 12), bg="#009688", fg="white", pady=5)
total_score_button.grid(row=11, column=4, padx=(10, 0), pady=(10, 20))

# 添加结果显示区域
result_frame = tk.Frame(root)
result_frame.pack(side=tk.LEFT, padx=5, pady=5)

# 添加结果标题
result_title_label = tk.Label(result_frame, text="比赛结果", font=("Arial", 16, "bold"))
result_title_label.pack(pady=(0, 10))

# 添加结果表格
result_table_frame = tk.Frame(result_frame)
result_table_frame.pack()

result_table_headers = ["名次", "参赛人员", "总得分"]

# 添加结果表头
for i, header in enumerate(result_table_headers):
    header_label = tk.Label(result_table_frame, text=header, font=("Arial", 12, "bold"), padx=10, pady=5)
    header_label.grid(row=0, column=i)

# 添加结果数据
for i in range(1, 11):
    # 添加名次
    rank_label = tk.Label(result_table_frame, text=str(i), font=("Arial", 4))
    rank_label.grid(row=i, column=0)

    # 添加参赛人员名称
    contestant_label = tk.Label(result_table_frame, text="参赛人员" + str(i), font=("Arial", 12))
    contestant_label.grid(row=i, column=1)

    # 添加总得分
    total_score_label = tk.Label(result_table_frame, text="0", font=("Arial", 12))
    total_score_label.grid(row=i, column=2)


# 添加参赛人员
def add_contestant():
    name = contestant_entry.get()
    if name:
        contestants_listbox.insert(tk.END, name)

# 添加评委
def add_judge():
    name = judge_entry.get()
    if name:
        judges_listbox.insert(tk.END, name)


# 计算总得分
def calculate_total_score():
    # 获取所有参赛人员
    contestants = contestants_listbox.get(0, tk.END)

    # 遍历所有参赛人员
    for index, contestant in enumerate(contestants):
        scores = []
        # 获取所有评委打分
        for j in range(2, 7):
            score = int(table_frame.grid_slaves(row=index + 1, column=j)[0].get())
            scores.append(score)

        # 计算总得分
        total_score = sum(scores) - min(scores) - max(scores)

        # 显示总得分
        total_score_label = table_frame.grid_slaves(row=index + 1, column=1)[0]
        total_score_label.configure(text=str(total_score))

        # 更新比赛结果
        result_table_frame.grid_slaves(row=index + 1, column=1)[0].configure(text=contestant)
        result_table_frame.grid_slaves(row=index + 1, column=2)[0].configure(text=str(total_score))


# 显示比赛结果
def show_result():
    # 获取所有参赛人员和总得分
    contestants = []
    for i in range(1, 11):
        contestant = result_table_frame.grid_slaves(row=i, column=1)[0].cget("text")
        total_score = result_table_frame.grid_slaves(row=i, column=2)[0].cget("text")
        contestants.append((contestant, total_score))

    # 按照总得分排序
    sorted_contestants = sorted(contestants, key=lambda x: int(x[1]), reverse=True)

    # 更新比赛结果表格
    for index, (contestant, total_score) in enumerate(sorted_contestants):
        result_table_frame.grid_slaves(row=index + 1, column=1)[0].configure(text=contestant)
        result_table_frame.grid_slaves(row=index + 1, column=2)[0].configure(text=total_score)


# 添加参赛人员输入框和按钮
contestant_frame = tk.Frame(root)
contestant_frame.pack(side=tk.TOP, padx=5, pady=5)

contestant_label = tk.Label(contestant_frame, text="参赛人员名称", font=("Arial", 12))
contestant_label.pack(side=tk.LEFT)

contestant_entry = tk.Entry(contestant_frame, font=("Arial", 12))
contestant_entry.pack(side=tk.LEFT, padx=5)

add_contestant_button = tk.Button(contestant_frame, text="添加参赛人员", font=("Arial", 12), bg="#009688", fg="white",
                                  command=add_contestant)
add_contestant_button.pack(side=tk.LEFT, padx=5)

# 添加评委输入框和按钮
judge_frame = tk.Frame(root)
judge_frame.pack(side=tk.TOP, padx=5, pady=5)

judge_label = tk.Label(judge_frame, text="评委名称", font=("Arial", 12))
judge_label.pack(side=tk.LEFT)

judge_entry = tk.Entry(judge_frame, font=("Arial", 12))
judge_entry.pack(side=tk.LEFT, padx=5)

add_judge_button = tk.Button(judge_frame, text="添加评委", font=("Arial", 12), bg="#009688", fg="white",
                             command=add_judge)
add_judge_button.pack(side=tk.LEFT, padx=5)

# 添加计算总得分和显示比赛结果按钮
function_frame = tk.Frame(root)
function_frame.pack(side=tk.TOP, padx=5, pady=5)

calculate_score_button = tk.Button(function_frame, text="计算总得分", font=("Arial", 12), bg="#009688", fg="white",
                                   padx=10, pady=5, command=calculate_total_score)
calculate_score_button.pack(side=tk.LEFT, padx=5)

show_result_button = tk.Button(function_frame, text="显示比赛结果", font=("Arial", 12), bg="#009688", fg="white",
                               padx=10, pady=5, command=show_result)
show_result_button.pack(side=tk.LEFT, padx=5)

# 运行界面
root.mainloop()
