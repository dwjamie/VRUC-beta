from application import db

genders = db.Enum('男', '女', '  ')
course_categories = db.Enum('学科基础', '专业必修', '专业选修', '跨学科专业选修', '              ')
departments = db.Enum('哲', '文', '历史', '国', '艺术', '外国语', '新闻', '农业与农村发展', '社会与人口',
                      '公共管理', '信息资源管理', '经济', '应用经济', '财政金融', '统计', '商', '劳动人事',
                      '中法', '法', '马克思主义', '国际关系', '环境', '信息', '理', '数学', '高瓴人工智能',
                      '              ')


class Teacher(db.Model):
    __tablename__ = '教师'

    id = db.Column('教职工号', db.Integer, primary_key=True)
    name = db.Column('姓名', db.String(10), nullable=False)
    gender = db.Column('性别', genders, nullable=False)
    phone_number = db.Column('电话', db.String(11), unique=True, nullable=False)
    email = db.Column('邮箱', db.String(30), unique=True, nullable=False)
    password = db.Column('密码', db.String(20), nullable=False)
    title = db.Column('职称', db.String(10), nullable=False)
    department = db.Column('所属学院', departments, nullable=False)

    def __repr__(self):
        return f'<教师 {self.id}>'


class Course(db.Model):
    __tablename__ = '课程'

    id = db.Column('课程号', db.Integer, primary_key=True)
    name = db.Column('课程名', db.String(50), nullable=False)
    category = db.Column('课程类别', course_categories, nullable=False)
    department = db.Column('开课学院', departments, nullable=False)
    credit = db.Column('学分', db.Integer, nullable=False)

    def __repr__(self):
        return f'<课程 {self.id}>'


class Class(db.Model):
    __tablename__ = '班级'

    id = db.Column('班级编号', db.Integer, primary_key=True)
    grade = db.Column('年级', db.Integer, nullable=False)
    index = db.Column('班号', db.Integer, nullable=False)
    department = db.Column('所属学院', departments, nullable=False)
    head_teacher_id = db.Column('班主任教职工号', db.Integer, db.ForeignKey('教师.教职工号'), nullable=False)
    head_teacher = db.relationship('Teacher', backref=db.backref('class_'))

    def __repr__(self):
        return f'<班级 {self.id}>'


class TeachingClass(db.Model):
    __tablename__ = '教学班'

    id = db.Column('教学班号', db.Integer, primary_key=True)
    teacher_id = db.Column('授课教师教职工号', db.Integer, db.ForeignKey('教师.教职工号'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('teaching_classes'))
    course_id = db.Column('课程号', db.Integer, db.ForeignKey('课程.课程号'), nullable=False)
    course = db.relationship('Course', backref=db.backref('teaching_classes'))
    semester = db.Column('开课学期', db.String(20), nullable=False)
    quota = db.Column('选课名额', db.Integer, nullable=False)

    def __repr__(self):
        return f'<教学班 {self.id}>'


class Student(db.Model):
    __tablename__ = '学生'

    id = db.Column('学号', db.Integer, primary_key=True)
    name = db.Column('姓名', db.String(10), nullable=False)
    gender = db.Column('性别', genders, nullable=False)
    phone_number = db.Column('电话', db.String(11), unique=True, nullable=False)
    email = db.Column('邮箱', db.String(30), unique=True, nullable=False)
    password = db.Column('密码', db.String(20), nullable=False)
    class_id = db.Column('所属班级编号', db.Integer, db.ForeignKey('班级.班级编号'), nullable=False)
    class_ = db.relationship('Class', backref=db.backref('students'))

    def __repr__(self):
        return f'<学生 {self.id}>'


class SC(db.Model):
    __tablename__ = '选课记录'

    student_id = db.Column('学号', db.Integer, db.ForeignKey('学生.学号'), primary_key=True)
    student = db.relationship('Student', backref=db.backref('SCs'))
    teaching_class_id = db.Column('教学班号', db.Integer, db.ForeignKey('教学班.教学班号'), primary_key=True)
    teaching_class = db.relationship('TeachingClass', backref=db.backref('SCs'))
    grade = db.Column('成绩', db.Float)
    teaching_quality_rating = db.Column('教学质量评分', db.Float)

    def __repr__(self):
        return f'<选课记录 {self.student_id} {self.teaching_class_id}>'
