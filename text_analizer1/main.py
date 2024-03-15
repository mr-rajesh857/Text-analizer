from flask import Flask,render_template,request

app=Flask(__name__)

@app.get("/")
def show():
    return render_template("index.html")

@app.post("/Analizer")
def analize():
    text=request.form["text"]    
    option=request.form["action"]
    ans=""
    if option=='cntchr':
        ans=f"The no. of characters are {len(text)} "
    elif option=='cntspc':
        ans=f"The total no of Spaces are {text.count(" ")}"
    # elif option==''
    return render_template("index.html",Output=ans)
if(__name__== "__main__"):
    app.run(debug=True)





