from django.shortcuts import render,redirect
from .models import Employee,Employee1 as emp1,Department,Query
from django.http import HttpResponse 
from django.core.mail import send_mail

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def registration(req):
      #   print(req.method)
      #   print(req.POST)
      #   print(req.FILES)

        if req.method =='POST':
              n = req.POST.get('name')
              e = req.POST.get('email')
              c = req.POST.get('contact')
              g = req.POST.get('gender')
              q = req.POST.getlist('qualification[]')
              s = req.POST.get('state')
              i = req.FILES.get('image')
              a = req.FILES.get('audio')
              v = req.FILES.get('video')
              d = req.FILES.get('document')
              p = req.POST.get('password')
              cp = req.POST.get('cpassword')

              print(n,e,c,g,q,s,i,a,v,d,p,cp,sep='\n')

              user = Employee.objects.filter(email=e)

              if user:
                    req.session['msg']=f"{e} Email already exist"
                    return redirect('registration')
              else:
                    if p == cp:
                          Employee.objects.create(
                                name=n,
                                email=e,
                                contact=c,
                                qualification=','.join(q),
                                gender=g,
                                state=s,
                                image=i,
                                video=v,
                                document=d,
                                password=p
                          )
                          req.session['pqr']="Registration done"
                          return redirect('login')
                    else:
                          req.session['xyz']="Password and confirm password not matched"
                          return redirect('registration')
                                    
        else:
              msg = req.session.get('msg','')
              xyz = req.session.get('xyz','')
              signup = req.session.get('signup','')
              req.session.flush()
              return render(req,'registration.html',{'msg':msg,'xyz':xyz,'signup':signup}) 


def show_data(req):
      data=Employee.objects.all()
      # data=Employee.objects.get(id=1)
      # data=Employee.objects.first()
      # data=Employee.objects.last()
      # data=Employee.objects.latest('name')
      # data=Employee.objects.earliest('name')
      # data=Employee.objects.create()

      # data=Employee.objects.all()
      # data = Employee.objects.filter(gender="Female")
      # data = Employee.objects.exclude(gender="Female")
      # data = Employee.objects.order_by('gender')
      # data = Employee.objects.order_by('-name')
      # data = Employee.objects.values()
      # data = (
      #  Employee.objects
      #    .filter(state__in=['Delhi','Maharashtra','Karnataka'])
      #    .exclude(gender="Female")
      #    .order_by("id")
      #      .reverse()
      #   )                      

      return render(req,'show_data.html',{'data':data})


# def login(req):
#     if req.method=='POST':
#           e = req.POST.get('email')
#           p = req.POST.get('password')
#           print(e,p)
#           user = Employee.objects.filter(email = e)
#           if not user:
#                 req.session['signup'] = f'Given email {e} is not register'
#                 return redirect('registration')
#           else:
#                 userdata = Employee.objects.get(email=e)
#                 print(userdata.id)
#
#                 db_pass = userdata.password
#                 print(db_pass)
#                 print(type(db_pass))
#                 if p == db_pass:
#                       req.session['user_id'] = userdata.id
#                       print(req.session['user_id'])
#                       return redirect('dashboard') 
#     pqr = req.session.get('pqr','')
#     req.session.flush()
#     return render(req, 'login.html',{'pqr':pqr})


def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e,p)
        if e == 'mahak.saxena550@gmail.com' and p == 'Mahak@123':
            data={
                 'name':'MAHAK SAXENA',
                 'Email':e,
                 'contact':'9713552550',
            }

            req.session['admin']=data
            return redirect('dashboard')
        else:
            user = emp1.objects.filter(email=e)
    
            if not user:
                req.session['signup'] = f'Given email {e} is not registered'
                return redirect('registration')
            else:
                  userdata = emp1.objects.get(email=e)
                  if p == userdata.password:
                        req.session['user_id'] = userdata.id
                        return redirect('userdashboard')
                  else:
                        req.session['signup'] = 'Wrong password'
                        return redirect('login')

    pqr = req.session.get('pqr','')
    req.session.flush()
    return render(req, 'login.html', {'pqr': pqr})


def dashboard(req):

    if req.session.get('admin', None):
        data = req.session.get('admin')
        return render(req, 'admin_dashboard.html', {'data': data})

    elif req.session.get('user_id', None):
        data = req.session.get('user_id')
        userdata = Employee.objects.get(id=data)
        return render(req, 'dashboard.html', {'data': userdata})

    else:
        return redirect('login')


def add_emp(req):
      if 'admin' not in req.session:
            print('admin not in login')
            return redirect('login')
      else:
            print("Add emp")
            if req.method=='POST':
                 n=req.POST.get('name')
                 e=req.POST.get('email')
                 c=req.POST.get('contact')
                 i=req.FILES.get('image') 
                 p=req.POST.get('password')
                 cp=req.POST.get('cpassword')
                 dep = req.POST.get('department')
                 dep_data = Department.objects.get(id=dep)
                 d_name=dep_data.department
                 d_code=dep_data.dept_code
                 d_des=dep_data.description

                 print(n, e, c, p,dep)

                 if p != cp:
                      req.session['msg']='Password not matched'
                      return redirect('add_emp')

                 user = emp1.objects.filter(email=e)
                 if not user:
                      emp1.objects.create(
                            name=n,
                            email=e,
                            contact=c,
                            image=i,
                            password=p,
                            department=d_name,
                            d_code=d_code,
                            d_des=d_des
                      )
                      send_mail(
                            'Employee Account Created',
                            f'your user id is {e} and password is {p}',
                            'mahak.saxena55@gmail.com',
                            [e],
                            fail_silently=False
                      )
                      req.session['msg']='employee created and mail has been sent'
                      return redirect('add_emp')
                 else:
                      req.session['msg']='user already exists'
                      return redirect('add_emp')

            msg=req.session.pop('msg',None)
            all_dept = Department.objects.all()
            return render(req,'admin_dashboard.html',{
                  'msg':msg,
                  'add_emp':True,
                  'data':req.session.get('admin'),
                  'all_dept':all_dept
            })


def add_dept(req):
    if 'admin' not in req.session:
        return redirect('login')

    if req.method == 'POST':
        dept_name = req.POST.get('department').strip()
        dept_code = req.POST.get('dept_code').strip()
        description = req.POST.get('description')

        exists = Department.objects.filter(department__iexact=dept_name).exists() or Department.objects.filter(dept_code__iexact=dept_code).exists()

        if exists:
            req.session['msg'] = 'Department name or code already exists!'
        else:
            Department.objects.create(
                department=dept_name,
                dept_code=dept_code,
                description=description
            )
            req.session['msg'] = 'Department added successfully'

        return redirect('add_dept')

    msg = req.session.get('msg')
    req.session.pop('msg', None)

    return render(req, 'admin_dashboard.html', {
        'add_dept': True,
        'data': req.session.get('admin'),
        'msg': msg
    })


def show_dept(req):
     if 'admin' not in req.session:
          return redirect('login')
     else:
          departments = Department.objects.all()
          return render(req,'admin_dashboard.html',{
                'show_dept':True,
                'departments':departments,
                'data':req.session.get('admin')
          })

def edit_dept(req,pk):
     if 'admin' not in req.session:
          return redirect('login')
     dept=Department.objects.get(id=pk)
     return render(req,'admin_dashboard.html',{'data':req.session.get('admin'),'edit_dept':True,'dept':dept})

def update_dept(req, pk):
    if 'admin' not in req.session:
        return redirect('login')
    dept = Department.objects.get(id=pk)
    dept.department = req.POST.get('department')
    dept.dept_code = req.POST.get('dept_code')
    dept.description = req.POST.get('description')
    dept.save()
    return redirect('show_dept')



def show_emp(req):
     if 'admin' not in req.session:
          return redirect('login')
     else:
          employees = emp1.objects.all()
          return render(req,'admin_dashboard.html',{
                'show_emp':True,
                'employees':employees,
                'data':req.session.get('admin')
          })

def edit_emp(req, pk):
    if 'admin' not in req.session:
        return redirect('login')
    emp = emp1.objects.get(id=pk)
    departments = Department.objects.all()
    return render(req, 'admin_dashboard.html', {
        'data': req.session.get('admin'),
        'edit_emp': True,
        'emp': emp,
        'departments': departments
    })

def update_emp(req, pk):
    if 'admin' not in req.session:
        return redirect('login')
    emp = emp1.objects.get(id=pk)
    if req.method == 'POST':
        emp.name = req.POST.get('name')
        emp.email = req.POST.get('email')
        emp.contact = req.POST.get('contact')
        dep_id = req.POST.get('department')
        dep = Department.objects.get(id=dep_id)
        emp.department = dep.department
        emp.d_code = dep.dept_code
        emp.d_des = dep.description
        if req.FILES.get('image'):
            emp.image = req.FILES.get('image')
        emp.save()
    return redirect('show_emp')




def show_query(req):
     if 'admin' not in req.session:
          return redirect('login')
     else:
          queries = Query.objects.all().order_by('created_at')
          return render(req,'admin_dashboard.html',{
                'show_query':True,
                'queries':queries,
                'data':req.session.get('admin')
          })


def delete(req,id):
     if 'admin' not in req.session:
          return redirect('login')
     data=emp1.objects.get(id=id)
     data.delete()
     return redirect('show_emp')

def delete_dept(req,id):
     if 'admin' not in req.session:
          return redirect('login')
     data=Department.objects.get(id=id)
     data.delete()
     return redirect('show_dept')

def reply_query(req,id):
     if 'admin' in req.session:
        data = req.session.get('admin')
        if req.method=='POST':
             r = req.POST.get('reply')
             querydata = Query.objects.get(id=id)
             if len(r)>1:
               querydata.solution = r
               querydata.status="Done"
               querydata.save()
               queries = Query.objects.all().order_by('created_at')
               return render(req,'admin_dashboard.html',{
                'show_query':True,
                'queries':queries,
                'data':req.session.get('admin')
               })
     
        else:
             return render(req, 'admin_dashboard.html', {'data': data,'reply':True,'id':id})

def logout(req):
      req.session.flush()
      return redirect('login')


def userdashboard(req):
     if 'user_id' in req.session:
        #   id=req.session.get('user_id')
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          return render(req,'userdashboard.html',{'data':userdata})

def profile(req):
     if  'user_id' in req.session:
          id = req.session['user_id']
          userdata=emp1.objects.get(id=id)
          return render (req,'userdashboard.html',{'data':userdata,'profile':True})
     else:
          return redirect('login')

def query(req):
     if 'user_id' in req.session:
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          return render (req,'userdashboard.html',{'data':userdata,'query':True})
     else:
          return redirect('login')
     
def query_status(req):
     if 'user_id' in req.session:
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          query_data=Query.objects.filter(email=userdata.email)
          return render (req,'userdashboard.html',{'data':userdata,'query_status':query_data})
     else:
          return redirect('login')

def all_query(req):
     if 'user_id' in req.session:
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          a_query=Query.objects.filter(email=userdata.email)
          return render (req,'userdashboard.html',{'data':userdata,'all_query':a_query})
     else:
          return redirect('login')

def query_data(req):
      if 'user_id' in req.session:
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          if req.method=='POST':
               n=req.POST.get('name')
               e=req.POST.get('email')
               s=req.POST.get('subject')
               q=req.POST.get('query')
               solu=req.POST.get('reply','pending')
               print(n,e,s,q,sep=',')
               Query.objects.create(name=n,email=e,subject=s,message=q,solution=solu)
            #    return render (req,'userdashboard.html',{'data':userdata})
               
               return render (req,'userdashboard.html',{'data':userdata,'query':True})
      else:
          return redirect('login')
      
def edit_query(req,pk):
     if "user_id" in req.session:
          id=req.session['user_id']
          userdata=emp1.objects.get(id=id)
          query=Query.objects.get(id=pk)
          return render (req,'userdashboard.html',{'userdata':userdata,'e_query':query})
     else:
          return redirect('login')

    
    
def Update_query(req,pk):
    if 'user_id' in req.session:
        id=req.session.get('user_id')
        query=Query.objects.get(id=pk)
        query.name=req.POST.get('name')
        query.email=req.POST.get('email')
        query.subject=req.POST.get('subject')
        query.message=req.POST.get('query')
        query.save()
        userdata=emp1.objects.get(id=id)
        queries = Query.objects.filter(email=userdata.email)
        return render(req,'userdashboard.html',{'data':userdata,'all_query':all_query,'queries': queries})
    else:
         return redirect('login')
    
def search(req):
     if not 'user_id' in req.session:
          return redirect('login')
     user_id=req.session.get('user_id')
     data=emp1.objects.get(id=user_id)
     s=req.POST.get('search')
     f_qdata=Query.objects.filter(name=s,message=s,status=s)

     # if 'user_id' in req.session:
     #      id=req.session['user_id']
     #      userdata=emp1.objects.get(id=id)
     #      a_query=Query.objects.filter(email=userdata.email)
     #      return render (req,'userdashboard.html',{'data':userdata,'all_query':a_query})
     # else:
     #      return redirect('login')
