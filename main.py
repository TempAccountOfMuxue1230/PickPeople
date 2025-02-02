from functions import *
import maliang as ml
import maliang.extensions as ml_ext

# Initialize window
root = ml.Tk((720, 360), title="抽人")
root.center()
root.resizable(False, False)
root.topmost(True)
root.at_exit(ml_ext.utils.get_exit_ask_function(root), ensure_destroy=False)

# Initialize base canvas
cav = ml.Canvas(root, bg="white")
cav.place(width=720, height=360)

# Initialize header canvas
header_cav = ml.Canvas(cav, bg="white")
header_cav.place(width=720, height=60, y=0)

# Initialize body canvas
sub_cav_1 = ml.Canvas(cav, bg="white")
sub_cav_1.place(width=720, height=300, x=0, y=60)
sub_cav_2 = ml.Canvas(cav, bg="white")
sub_cav_2.place(width=720, height=300, x=720, y=60)

# Place things to header cav
ml.SegmentedButton(header_cav, (260, 10), ((100, 30), (100, 30)), text=("抽 人", "抽 卡"), default=0, command=get_pick(root, sub_cav_1, sub_cav_2))
ml_ext.IconOnlyButton(header_cav, (720, 0), (60, 60), image=ml.PhotoImage(file=resource_path("assets\\icon.png")), anchor="ne")

# Place things to "Pick People" Page
t1 = ml.Text(sub_cav_1, (360, 100), text="【等待抽人】", fontsize=60, anchor="center")
ml.Button(sub_cav_1, (210, 200), (300, 50), text="点击开始抽人", command=get_pick_people(root, sub_cav_1, t1))

# Place things to "Pick Card" Page
ml.Text(sub_cav_2, (10, 10), text="当前Up：S凌云，A瑞兴、A泠诗韩", fontsize=20)
t2 = ml.Text(sub_cav_2, (360, 100), text="【点击抽卡】", fontsize=60, anchor="center")
ml.Button(sub_cav_2, (135, 200), (140, 50), text="抽一次", command=get_pick_card(root, sub_cav_2, t2, 0))
ml.Button(sub_cav_2, (295, 200), (140, 50), text="抽十次", command=get_pick_card(root, sub_cav_2, t2, 1)).disable(True)
ml.Button(sub_cav_2, (445, 200), (140, 50), text="评  估").disable(True)

# Main Loop
root.mainloop()
