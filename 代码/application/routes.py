from flask import render_template, url_for, redirect, request, session, flash
from flask import current_app as app
from .models import *
import matplotlib.pyplot as plt
import random


@app.route('/')
@app.route('/登录', methods=('POST', 'GET'))
def login():
    # teacher_1 = Teacher(id=200001,
    #                     name='周静',
    #                     gender='女',
    #                     phone_number='18812345678',
    #                     email='zhoujing@ruc.edu.cn',
    #                     password='password1234',
    #                     title='助理教授',
    #                     department='统计')
    #
    # teacher_2 = Teacher(name='尹建鑫',
    #                     gender='男',
    #                     phone_number='18812345679',
    #                     email='yinjianxin@ruc.edu.cn',
    #                     password='password1234',
    #                     title='副教授',
    #                     department='统计')
    #
    # teacher_3 = Teacher(name='覃雄派',
    #                     gender='男',
    #                     phone_number='18812345680',
    #                     email='qinxiongpai@ruc.edu.cn',
    #                     password='password1234',
    #                     title='副教授',
    #                     department='信息')
    #
    # teacher_4 = Teacher(name='党之玉',
    #                     gender='女',
    #                     phone_number='18812345681',
    #                     email='dangzhiyu@ruc.edu.cn',
    #                     password='password1234',
    #                     title='教务秘书',
    #                     department='统计')
    #
    # course_1 = Course(id=100001,
    #                   name='深度学习',
    #                   category='专业选修',
    #                   department='统计',
    #                   credit=3)
    #
    # course_2 = Course(name='概率论',
    #                   category='学科基础',
    #                   department='统计',
    #                   credit=4)
    #
    # course_3 = Course(name='数据库系统概论',
    #                   category='学科基础',
    #                   department='统计',
    #                   credit=4)
    #
    # course_4 = Course(name='数理统计',
    #                   category='专业必修',
    #                   department='统计',
    #                   credit=4)
    #
    # course_5 = Course(name='宏观经济学',
    #                   category='跨学科专业选修',
    #                   department='经济',
    #                   credit=3)
    #
    # class_1 = Class(id=100001,
    #                 grade=2018,
    #                 index=4,
    #                 department='统计',
    #                 head_teacher_id=200001)
    #
    # class_2 = Class(grade=2018,
    #                 index=1,
    #                 department='统计',
    #                 head_teacher_id=200002)
    #
    # teaching_class_1 = TeachingClass(id=100001,
    #                                  teacher_id=200001,
    #                                  course_id=100001,
    #                                  semester='2020-2021 秋季学期',
    #                                  quota=40)
    #
    # teaching_class_2 = TeachingClass(teacher_id=200002,
    #                                  course_id=100002,
    #                                  semester='2019-2020 秋季学期',
    #                                  quota=120)
    #
    # teaching_class_3 = TeachingClass(teacher_id=200003,
    #                                  course_id=100003,
    #                                  semester='2019-2020 春季学期',
    #                                  quota=80)
    #
    # student_1 = Student(id=100001,
    #                     name='老番茄',
    #                     gender='男',
    #                     phone_number=18887654321,
    #                     email='laofanqie@ruc.edu.cn',
    #                     password='password1234',
    #                     class_id=100001)
    #
    # student_2 = Student(name='某幻君',
    #                     gender='男',
    #                     phone_number=18887654322,
    #                     email='mouhuanjun@ruc.edu.cn',
    #                     password='password1234',
    #                     class_id=100001)
    #
    # student_3 = Student(name='中国博爱',
    #                     gender='男',
    #                     phone_number=18887654323,
    #                     email='zhongguoboai@ruc.edu.cn',
    #                     password='password1234',
    #                     class_id=100001)
    #
    # student_4 = Student(name='花少北',
    #                     gender='男',
    #                     phone_number=18887654324,
    #                     email='huashaobei@ruc.edu.cn',
    #                     password='password1234',
    #                     class_id=100001)
    #
    # student_5 = Student(name='蕾克斯班纳',
    #                     gender='男',
    #                     phone_number=18887654325,
    #                     email='leikesibanna@ruc.edu.cn',
    #                     password='password1234',
    #                     class_id=100001)
    #
    # sc_1 = SC(student_id=100001,
    #           teaching_class_id=100001)
    #
    # sc_2 = SC(student_id=100002,
    #           teaching_class_id=100002,
    #           grade=80,
    #           teaching_quality_rating=90)
    #
    # sc_3 = SC(student_id=100004,
    #           teaching_class_id=100003,
    #           grade=95,
    #           teaching_quality_rating=100)
    #
    # db.session.add(teacher_1)
    # db.session.add(teacher_2)
    # db.session.add(teacher_3)
    # db.session.add(teacher_4)
    # db.session.add(course_1)
    # db.session.add(course_2)
    # db.session.add(course_3)
    # db.session.add(course_4)
    # db.session.add(course_5)
    # db.session.commit()
    #
    # db.session.add(class_1)
    # db.session.add(class_2)
    # db.session.commit()
    #
    # db.session.add(teaching_class_1)
    # db.session.add(teaching_class_2)
    # db.session.add(teaching_class_3)
    # db.session.commit()
    #
    # db.session.add(student_1)
    # db.session.add(student_2)
    # db.session.add(student_3)
    # db.session.add(student_4)
    # db.session.add(student_5)
    # db.session.commit()
    #
    # db.session.add(sc_1)
    # db.session.add(sc_2)
    # db.session.add(sc_3)
    # db.session.commit()

    if request.method == 'POST':
        _id = int(request.form['id'])
        password = request.form['password']

        if 100000 < _id < 200000:
            found_student = Student.query.get(_id)
            if found_student and found_student.password == password:
                session['user_id'] = _id
                session['user_type'] = 'student'
                flash('登录成功！')
                return redirect(url_for('index'))
        elif 200000 < _id < 300000:
            found_teacher = Teacher.query.get(_id)
            if found_teacher and found_teacher.password == password:
                session['user_id'] = _id
                if found_teacher.title == '教务秘书':
                    session['user_type'] = 'admin'
                else:
                    session['user_type'] = 'teacher'
                flash('登录成功！')
                return redirect(url_for('index'))

        flash('学号/教职工号或密码错误，请重新登录！')
        return redirect(url_for('login'))

    if 'user_id' in session:
        return redirect(url_for('index'))

    return render_template('登录.html')


@app.route('/登出')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        session.pop('user_type')
        flash('您已成功登出！')

    return redirect(url_for('login'))


@app.route('/主页')
def index():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    user_type = session['user_type']

    if user_type == 'student':
        user_name = Student.query.get(session['user_id']).name
    else:
        user_name = Teacher.query.get(session['user_id']).name

    return render_template('主页.html',
                           user_name=user_name,
                           user_type=user_type)


@app.route('/个人信息')
def info():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    user_type = session['user_type']

    if user_type == 'student':
        user = Student.query.get(session['user_id'])

        return render_template('个人信息.html',
                               user_id=session['user_id'],
                               user_name=user.name,
                               user_gender=user.gender,
                               user_phone_number=user.phone_number,
                               user_email=user.email,
                               user_grade=user.class_.grade,
                               user_class_index=user.class_.index,
                               user_department=user.class_.department,
                               user_head_teacher_name=user.class_.head_teacher.name,
                               user_type=user_type)
    else:
        user = Teacher.query.get(session['user_id'])

        if user.class_:
            user_class_index = user.class_[0].index
        else:
            user_class_index = None

        return render_template('个人信息.html',
                               user_id=session['user_id'],
                               user_name=user.name,
                               user_gender=user.gender,
                               user_phone_number=user.phone_number,
                               user_email=user.email,
                               user_title=user.title,
                               user_department=user.department,
                               user_class_index=user_class_index,
                               user_teaching_courses=set([teaching_class.course.name for teaching_class in user.teaching_classes]),
                               user_type=user_type)


@app.route('/修改密码', methods=('POST', 'GET'))
def password_change():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if request.method == 'POST':
        if session['user_type'] == 'student':
            user = Student.query.get(session['user_id'])
        else:
            user = Teacher.query.get(session['user_id'])

        if request.form['old_password'] != user.password:
            flash('原密码错误，请重试！')
        elif request.form['new_password'] != request.form['repeat_new_password']:
            flash('两次输入的新密码不一致，请重试！')
        else:
            user.password = request.form['new_password']
            flash('密码修改成功！')

        return redirect(url_for('password_change'))
    else:
        return render_template('修改密码.html')


@app.route('/主页/选课', methods=('POST', 'GET'))
def course_register():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'student':
        user = Student.query.get(session['user_id'])

        selectable_teaching_classes = TeachingClass.query.join(Course) \
            .filter(db.or_(Course.department == user.class_.department, Course.category == '跨学科专业选修'),
                    TeachingClass.semester == '2020-2021 秋季学期')

        quotas = [teaching_class.quota - len(teaching_class.SCs) for teaching_class in selectable_teaching_classes]
        n_row = len(quotas)

        selected_teaching_class_ids = [sc.teaching_class_id for sc in user.SCs]

        if request.method == 'POST':
            teaching_class_id = int(request.form['id'])
            found_teaching_class = TeachingClass.query.get(teaching_class_id)

            selectable_teaching_class_ids = [teaching_class.id for teaching_class in selectable_teaching_classes]

            if found_teaching_class:
                if teaching_class_id in selectable_teaching_class_ids:
                    if found_teaching_class.quota > 0:
                        if teaching_class_id not in selected_teaching_class_ids:
                            sc = SC(student_id=user.id, teaching_class_id=teaching_class_id)
                            db.session.add(sc)
                            db.session.commit()
                            flash('选课成功！')
                        else:
                            flash('您已选择过这个教学班，不能重复选课！')
                    else:
                        flash('名额已满，选课失败！')
                else:
                    flash('该教学班不可选，选课失败！')
            else:
                flash('不存在的教学班号，选课失败！')

            return redirect(url_for('course_register'))
        else:
            return render_template('选课.html', teaching_classes=selectable_teaching_classes, quotas=quotas,
                                   selected_teaching_class_ids=selected_teaching_class_ids, n_row=n_row)
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/退课', methods=('POST', 'GET'))
def course_unregister():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'student':
        user = Student.query.get(session['user_id'])
        selected_teaching_class_ids = [sc.teaching_class_id for sc in user.SCs]
        for i in reversed(range(len(selected_teaching_class_ids))):
            if TeachingClass.query.get(selected_teaching_class_ids[i]).semester != '2020-2021 秋季学期':
                selected_teaching_class_ids.pop(i)
        selected_teaching_classes = [TeachingClass.query.get(id_) for id_ in selected_teaching_class_ids]

        if request.method == 'POST':
            teaching_class_id = int(request.form['id'])

            found_teaching_class = TeachingClass.query.get(teaching_class_id)

            if found_teaching_class:
                if teaching_class_id in selected_teaching_class_ids:
                    SC.query.filter_by(student_id=user.id, teaching_class_id=teaching_class_id).delete()
                    db.session.commit()
                    flash('退课成功！')
                else:
                    flash('您未选择此教学班，退课失败！')
            else:
                flash('不存在的教学班号，退课失败！')

            return redirect(url_for('course_unregister'))
        else:
            return render_template('退课.html', selected_teaching_classes=selected_teaching_classes)
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


def label_count(list_, label):
    count = 0
    for item in list_:
        if item == label:
            count += 1
    return count


@app.route('/主页/选课历史', methods=('POST', 'GET'))
def course_register_history():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    user_type = session['user_type']
    if user_type == 'student':
        user = Student.query.get(session['user_id'])
        SCs = list(user.SCs)

        if len(SCs) > 0:
            categories = [sc.teaching_class.course.category for sc in SCs]
            labels = ['学科基础', '专业必修', '专业选修', '跨学科专业选修']
            counts = [label_count(categories, label) for label in labels]

            plt.title('各类课程选修数量')
            plt.bar(range(len(labels)), counts)
            plt.xticks(range(len(labels)), labels)
            plt.savefig('./Application/static/images/各类课程选修数量.png', dpi=120)
            plt.clf()

            have_fig = True
        else:
            have_fig = False

        if request.method == 'POST':
            semester = request.form['semester']
            category = request.form['category']

            if semester == '本学期':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.semester != '2019-2020 春季学期':
                        SCs.pop(i)
            elif semester == '本学年':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.semester not in ['2019-2020 秋季学期', '2019-2020 春季学期']:
                        SCs.pop(i)

            if category != '全部':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.course.category != category:
                        SCs.pop(i)

            if len(SCs) > 0:
                categories = [sc.teaching_class.course.category for sc in SCs]
                labels = ['学科基础', '专业必修', '专业选修', '跨学科专业选修']
                counts = [label_count(categories, label) for label in labels]

                plt.title('各类课程选修数量')
                plt.bar(range(len(labels)), counts)
                plt.xticks(range(len(labels)), labels)
                plt.savefig('./Application/static/images/各类课程选修数量.png', dpi=120)
                plt.clf()

                have_fig = True
            else:
                have_fig = False

            return render_template('选课历史.html', SCs=SCs, options=[semester, category], have_fig=have_fig, random=random.random())
        else:
            return render_template('选课历史.html', SCs=SCs, options=['全部', '全部'], have_fig=have_fig, random=random.random())
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/全校课程表', methods=('POST', 'GET'))
def all_teaching_classes():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    teaching_classes = list(TeachingClass.query.all())

    if request.method == 'POST':
        semester = request.form['semester']
        category = request.form['category']

        if semester == '本学期':
            for i in reversed(range(len(teaching_classes))):
                if teaching_classes[i].semester != '2019-2020 春季学期':
                    teaching_classes.pop(i)
        elif semester == '本学年':
            for i in reversed(range(len(teaching_classes))):
                if teaching_classes[i].semester not in ['2019-2020 秋季学期', '2019-2020 春季学期']:
                    teaching_classes.pop(i)

        if category != '全部':
            for i in reversed(range(len(teaching_classes))):
                if teaching_classes[i].course.category != category:
                    teaching_classes.pop(i)

        return render_template('全校课程表.html', teaching_classes=teaching_classes, options=[semester, category])
    else:
        return render_template('全校课程表.html', teaching_classes=teaching_classes, options=['全部', '全部'])


def grade2gpa(grade):
    if grade < 0 or grade > 100:
        return -1
    elif grade >= 90:
        return 4
    elif grade >= 86:
        return 3.7
    elif grade >= 83:
        return 3.3
    elif grade >= 80:
        return 3
    elif grade >= 76:
        return 2.7
    elif grade >= 73:
        return 2.3
    elif grade >= 70:
        return 2
    elif grade >= 66:
        return 1.7
    elif grade >= 63:
        return 1.3
    elif grade >= 60:
        return 1
    else:
        return 0


@app.route('/主页/成绩查询', methods=('POST', 'GET'))
def grade_query():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'student':
        user = Student.query.get(session['user_id'])
        SCs = list(user.SCs)
        for i in reversed(range(len(SCs))):
            if SCs[i].grade is None or SCs[i].teaching_class.semester == '2020-2021 秋季学期':
                SCs.pop(i)

        if len(SCs) > 0:
            total_grade = sum([sc.grade for sc in SCs])
            total_credit = sum([sc.teaching_class.course.credit for sc in SCs])
            total_gpa = sum([grade2gpa(sc.grade) * sc.teaching_class.course.credit for sc in SCs])

            data = [sc.grade for sc in SCs]
            plt.title('各科成绩分布')
            plt.hist(data)
            plt.xlabel('分数')
            plt.ylabel('频数')
            plt.savefig('./Application/static/images/各科成绩分布.png', dpi=120)
            plt.clf()

            gpa = total_gpa / total_credit
            ave_grade = total_grade / len(SCs)
            have_fig = True
        else:
            gpa = -1
            ave_grade = -1
            have_fig = False

        if request.method == 'POST':
            semester = request.form['semester']
            category = request.form['category']

            if semester == '本学期':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.semester != '2019-2020 春季学期':
                        SCs.pop(i)
            elif semester == '本学年':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.semester not in ['2019-2020 秋季学期', '2019-2020 春季学期']:
                        SCs.pop(i)

            if category != '全部':
                for i in reversed(range(len(SCs))):
                    if SCs[i].teaching_class.course.category != category:
                        SCs.pop(i)

            if len(SCs) > 0:
                total_grade = sum([sc.grade for sc in SCs])
                total_credit = sum([sc.teaching_class.course.credit for sc in SCs])
                total_gpa = sum([grade2gpa(sc.grade) * sc.teaching_class.course.credit for sc in SCs])

                data = [sc.grade for sc in SCs]
                plt.title('各科成绩分布')
                plt.hist(data)
                plt.xlabel('分数')
                plt.ylabel('频数')
                plt.savefig('./Application/static/images/各科成绩分布.png', dpi=120)
                plt.clf()

                gpa = total_gpa / total_credit
                ave_grade = total_grade / len(SCs)
                have_fig = True
            else:
                gpa = -1
                ave_grade = -1
                have_fig = False

            return render_template('成绩查询.html', SCs=SCs, options=[semester, category], gpa=gpa, ave_grade=ave_grade,
                                   have_fig=have_fig, random=random.random())
        else:
            return render_template('成绩查询.html', SCs=SCs, options=['全部', '全部'], gpa=gpa, ave_grade=ave_grade,
                                   have_fig=have_fig, random=random.random())
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/注册教学班', methods=('POST', 'GET'))
def teaching_class_register():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'teacher':
        if request.method == 'POST':
            course_id = int(request.form['course_id'])
            semester = request.form['semester']
            quota = int(request.form['quota'])

            found_course = Course.query.get(course_id)

            if found_course:
                teaching_class = TeachingClass(teacher_id=session['user_id'], course_id=course_id, semester=semester,
                                               quota=quota)
                db.session.add(teaching_class)
                db.session.commit()
                flash('教学班注册成功！')
            else:
                flash('课程号不存在！')

            return redirect(url_for('teaching_class_register'))
        else:
            return render_template('注册教学班.html')
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/所有课程', methods=('POST', 'GET'))
def all_courses():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    courses = list(Course.query.all())

    if request.method == 'POST':
        category = request.form['category']
        department = request.form['department']

        if category != '全部':
            for i in reversed(range(len(courses))):
                if courses[i].category != category:
                    courses.pop(i)

        if department != '全部':
            for i in reversed(range(len(courses))):
                if courses[i].department != department:
                    courses.pop(i)

        return render_template('所有课程.html', courses=courses, option=category)
    else:
        return render_template('所有课程.html', courses=courses, option='全部')


@app.route('/主页/班级管理')
def class_management():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'teacher':
        user = Teacher.query.get(session['user_id'])

        found_class = user.class_

        if found_class:
            students = list(user.class_[0].students)

            if len(students) > 0:
                gpa_list = []
                n_students_with_grade = 0
                for student in students:
                    SCs = list(student.SCs)
                    for i in reversed(range(len(SCs))):
                        if SCs[i].grade is None or SCs[i].teaching_class.semester == '2020-2021 秋季学期':
                            SCs.pop(i)

                    if len(SCs) > 0:
                        total_gpa = sum([grade2gpa(sc.grade) * sc.teaching_class.course.credit for sc in SCs])
                        total_credit = sum([sc.teaching_class.course.credit for sc in SCs])

                        gpa = total_gpa / total_credit
                        gpa_list.append(gpa)

                        n_students_with_grade += 1

                if n_students_with_grade > 0:
                    ave_gpa = sum(gpa_list) / n_students_with_grade
                    max_gpa = max(gpa_list)
                    min_gpa = min(gpa_list)

                    plt.title('班级GPA分布')
                    plt.hist(gpa_list)
                    plt.xlabel('GPA')
                    plt.ylabel('频数')
                    plt.savefig('./Application/static/images/班级GPA分布.png', dpi=120)
                    plt.clf()

                    have_fig = True
                else:
                    ave_gpa = -1
                    max_gpa = -1
                    min_gpa = -1
                    have_fig = False

                return render_template('班级管理.html', students=students, ave_gpa=ave_gpa, max_gpa=max_gpa,
                                       min_gpa=min_gpa, have_fig=have_fig, random=random.random())
            else:
                flash('您的班级中尚没有学生！')
                return redirect(url_for('index'))
        else:
            flash('您没有管辖班级！')
            return redirect(url_for('index'))
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/教师注册', methods=('POST', 'GET'))
def teacher_register():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            phone_number = request.form['phone_number']
            email = request.form['email']
            title = request.form['title']
            department = request.form['department']

            if name and phone_number and email and title and gender != '请选择...' and department != '请选择...':
                teacher = Teacher(name=name, gender=gender, phone_number=phone_number, email=email, title=title,
                                  department=department, password='password1234')
                db.session.add(teacher)
                db.session.commit()
                flash('教师注册成功！')
            else:
                flash('信息填写不全，请重新填写！')

            return redirect(url_for('teacher_register'))
        else:
            return render_template('教师注册.html')
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/学生注册', methods=('POST', 'GET'))
def student_register():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            phone_number = request.form['phone_number']
            email = request.form['email']
            class_id = int(request.form['class_id'])

            if name and phone_number and email and class_id and gender != '请选择...':
                found_class = Class.query.get(class_id)

                if found_class:
                    student = Student(name=name, gender=gender, phone_number=phone_number, email=email,
                                      class_id=class_id,
                                      password='password1234')
                    db.session.add(student)
                    db.session.commit()
                    flash('学生注册成功！')
                else:
                    flash('班级不存在，请重新填写！')
            else:
                flash('信息填写不全，请重新填写！')

            return redirect(url_for('student_register'))
        else:
            return render_template('学生注册.html')
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))


@app.route('/主页/课程注册', methods=('POST', 'GET'))
def course_add():
    if 'user_id' not in session:
        flash('请先登录！')
        return redirect(url_for('login'))

    if session['user_type'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            category = request.form['category']
            department = request.form['department']
            credit = int(request.form['credit'])

            if name and credit and category != '请选择...' and department != '请选择...':
                course = Course(name=name, category=category, department=department, credit=credit)
                db.session.add(course)
                db.session.commit()
                flash('课程注册成功！')
            else:
                flash('信息填写不全，请重新填写！')

            return redirect(url_for('course_add'))
        else:
            return render_template('课程注册.html')
    else:
        flash('您没有权限访问！')
        return redirect(url_for('index'))