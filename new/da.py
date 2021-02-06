

import webbrowser
import pandas as pd



webbrowser.open_new_tab('https://drive.google.com/file/d/1jpxjSI-N0XrVhTq4Nq5ctjGO7tkuU_Ot/view?usp=sharing')
webbrowser.open_new('https://drive.google.com/file/d/1jpxjSI-N0XrVhTq4Nq5ctjGO7tkuU_Ot/view?usp=sharing')




#driver.get(w)
q={'stckname':stckname}
exec(open('LinearRegression.py').read(),q)
exec(open('SvmModel.py').read(),q)
exec(open('LogisticModel.py').read(),q)
exec(open('DecisionTree.py').read(),q)
exec(open('naive.py').read(),q)


