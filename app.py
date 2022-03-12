#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def xyz():
    return render_template('numadd.html')
@app.route('/abcd',methods=['POST'])
def abc():
    if(request.method=='POST'):
        num1=int(request.form['a'])
        num2=int(request.form['b'])
        o=num1+num2
        return render_template('numadd.html',total=o)
if __name__=='__main__':
    app.run()


# In[ ]:




