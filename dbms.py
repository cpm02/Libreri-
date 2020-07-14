from flask import Flask,render_template,request,url_for,flash
import sqlite3
dbms=Flask(__name__)

'''con=sqlite3.connect("bookshop.db")
print("Database opened successfully")
con.execute("create table BILL (Billid INTEGER NOT NULL, cid INTEGER NOT NULL,bookid INTEGER NOT NULL,quantity TEXT NOT NULL)")
con.execute("ALTER TABLE BILL ADD PRIMARY KEY (Billid,cid,bookid)")
con.execute("ALTER TABLE BILL ADD FOREIGN KEY (cid) REFERENCES CUSTOMER(cid),ADD FOREIGN KEY (bookid) REFERENCES BOOKS(Bookid)")'''

print("Table created successfully")

@dbms.route("/")
def init():
    return render_template("loginpage.html")


@dbms.route("/index1")
def index():
    return render_template("index1.html")

@dbms.route("/getbill")
def getbill():
    return render_template("getbill.html")




@dbms.route("/login",methods=["POST","GET"])
def login():
    user=request.form['uname']
    pas=request.form['pwd']
    if (user=='pragya' and pas== '123'):
        return render_template("index1.html")
    else:
        return render_template("loginpage.html")


@dbms.route("/book")
def book():
    return render_template("book.html")

@dbms.route("/customer")
def customer():
    return render_template("customer.html")

@dbms.route("/bill")
def bill():
    return render_template("bill.html")

@dbms.route("/displaybill",methods=["POST","GET"])
def displaybill():
    msg="msg"
    if request.method=="POST":
        try:
            cid=request.form["cid"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()
                con.row_factory = sqlite3.Row
                cur.execute("SELECT SUM(cost*quantity) FROM (BOOKS NATURAL JOIN (SELECT bookid,quantity FROM BILL WHERE cid = ?) AS T) GROUP BY bookid",(cid))
                rows = cur.fetchall()
                print(rows)
                return render_template("showbill.html",rows = rows)  
        except Exception as e:
            print(e) 
            con.rollback()
            msg = "We can not find"    
            return render_template("bill.html")
            con.commit()



@dbms.route("/search1")
def search1():
    return render_template("search1.html")

@dbms.route("/authsearch")
def authsearch():
    return render_template("authsearch.html")

@dbms.route("/gensearch")
def gensearch():
    return render_template("gensearch.html")

@dbms.route("/booksearch")
def booksearch():
    return render_template("booksearch.html")            





@dbms.route("/add1")
def add1():
    return render_template("add1.html")


@dbms.route("/add2")
def add2():
    return render_template("add2.html")   

@dbms.route("/add3")
def add3():
    return render_template("add3.html")


@dbms.route("/searchdetails1",methods=["POST","GET"])
def searchdetails1():
    msg="msg"
    if request.method=="POST":
        try:
            author=request.form["author"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()
                con.row_factory = sqlite3.Row
                cur.execute("select * from BOOKS WHERE author = '{}' ".format(author))
                msg = "book successfully searched" 
                rows = cur.fetchall()
                print(rows)
                return render_template("viewsearch.html",rows = rows)  
        except Exception as e:
            print(e) 
            con.rollback()
            msg = "We can not find"    
            return render_template("view1.html")
            con.commit()




@dbms.route("/searchdetails2",methods=["POST","GET"])
def searchdetails2():
    msg="msg"
    if request.method=="POST":
        try:
            genre=request.form["genre"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()
                con.row_factory = sqlite3.Row
                cur.execute("select * from BOOKS WHERE genre = '{}' ".format(genre))
                msg = "book successfully searched" 
                rows = cur.fetchall()
                print(rows)
                return render_template("viewsearch.html",rows = rows)  
        except Exception as e:
            print(e) 
            con.rollback()
            msg = "We can not find"    
            return render_template("view1.html")
            con.commit()



@dbms.route("/searchdetails3",methods=["POST","GET"])
def searchdetails3():
    msg="msg"
    if request.method=="POST":
        try:
            bookname=request.form["bookname"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()
                con.row_factory = sqlite3.Row
                cur.execute("select * from BOOKS WHERE bookname = '{}' ".format(bookname))
                msg = "book successfully searched" 
                rows = cur.fetchall()
                print(rows)
                return render_template("viewsearch.html",rows = rows)  
        except Exception as e:
            print(e) 
            con.rollback()
            msg = "We can not find"    
            return render_template("view1.html")
            con.commit()


@dbms.route("/savedetails",methods=["POST","GET"])
def saveDetails():
    msg="msg"
    if request.method=="POST":
        try:
            bookname=request.form["Book_name"]
            author= request.form["Book_Author"]  
            edition=request.form["Edition"]
            genre=request.form["Genre"]
            quantity= request.form["quantity"]
            cost= request.form["cost"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into BOOKS (bookname, author,genre,edition,quantity,cost) values (?,?,?,?,?,?)",(bookname,author,genre,edition,quantity,cost))  
                con.commit()  
                msg = "Books successfully Added" 
        except:  
            con.rollback()  
            msg = "We can not add the book to the list" 
        finally:  
            return render_template("success1.html",msg = msg)  
            con.commit()



@dbms.route("/savedetails2",methods=["POST","GET"])
def saveDetails2():
    msg="msg"
    if request.method=="POST":
        try:
            cname=request.form["c_name"]
            email= request.form["email"]  
            contact=request.form["contact_no"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into CUSTOMER (cname, email, contact) values (?,?,?)",(cname,email,contact))  
                con.commit()  
                msg = "Customer successfully Added" 
        except:  
            con.rollback()  
            msg = "We can not add the Customer to the list" 
        finally:  
            return render_template("success2.html",msg = msg)  
            con.commit()


@dbms.route("/savedetails3",methods=["POST","GET"])
def saveDetails3():
    msg="msg"
    if request.method=="POST":
        try:
            Billid=request.form["Billid"]
            cid= request.form["cid"]  
            bookid=request.form["bookid"]
            quantity=request.form["quantity"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into BILL (Billid, cid, bookid, quantity) values (?,?,?,?)",(Billid, cid, bookid, quantity))  
                con.commit()  
                msg = "Bill successfully Added" 
        except:  
            con.rollback()  
            msg = "We can not add the Bill to the list" 
        finally:  
            return render_template("success3.html",msg = msg)  
            con.commit()



@dbms.route("/view1")  
def view1():  
    con = sqlite3.connect("bookshop.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from BOOKS")  
    rows = cur.fetchall()  
    return render_template("view1.html",rows = rows)   


@dbms.route("/view2")  
def view2():  
    con = sqlite3.connect("bookshop.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from CUSTOMER")  
    rows = cur.fetchall()  
    return render_template("view2.html",rows = rows)

@dbms.route("/view3")  
def view3():  
    con = sqlite3.connect("bookshop.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from BILL")  
    rows = cur.fetchall()  
    return render_template("view3.html",rows = rows)

@dbms.route("/delete1")
def delete1():
    return render_template("delete1.html")

@dbms.route("/delete2")
def delete2():
    return render_template("delete2.html")

@dbms.route("/delete3")
def delete3():
    return render_template("delete3.html")



@dbms.route("/deleterecord1" ,methods=["POST","GET"])
def deleterecord1():
    msg="msg"
    if request.method=="POST":
        try:
            bookid=request.form["bookid"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("delete from BOOKS where bookid = ?",(bookid))  
                con.commit()  
                msg = "successfully deleted" 
        except EXception as e:  
            con.rollback()
            msg = "We can not delete"
            print(e) 
        finally:  
            return render_template("success1.html",msg = msg)  
            con.commit()

@dbms.route("/deleterecord2" ,methods=["POST","GET"])
def deleterecord2():
    msg="msg"
    if request.method=="POST":
        try:
            cid=request.form["cid"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("delete from CUSTOMER where cid = ?",(cid))  
                con.commit()  
                msg = "successfully deleted" 
        except EXception as e:  
            con.rollback()
            msg = "We can not delete"
            print(e) 
        finally:  
            return render_template("success2.html",msg = msg)  
            con.commit()

@dbms.route("/deleterecord3" ,methods=["POST","GET"])
def deleterecord3():
    msg="msg"
    if request.method=="POST":
        try:
            Billid=request.form["Billid"]
            with sqlite3.connect("bookshop.db") as con:  
                cur = con.cursor()  
                cur.execute("delete from BILL where Billid = ?",(Billid))  
                con.commit()  
                msg = "successfully deleted" 
        except EXception as e:  
            con.rollback()
            msg = "We can not delete"
            print(e) 
        finally:  
            return render_template("success3.html",msg = msg)  
            con.commit()

if __name__ == '__main__':
   dbms.run(debug = True)