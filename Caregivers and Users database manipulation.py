

#assignment2:
import random
from datetime import date, time


# Imporint things:
from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, ForeignKey, Date, Time, update, case, \
    literal_column, delete, and_, text, func, select
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, aliased

#Declaring base:
Base = declarative_base()
engine = create_engine('postgresql://postgres:0007@localhost:5432/Assignment2')

Session = sessionmaker(bind=engine)
session = Session()

#function to create tables:
def tables_all():
    Base.metadata.create_all(bind=engine)


#Declaring tables:
class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, unique=True, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    given_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    city = Column(String(50))
    phone_number = Column(String(15))
    profile_description = Column(Text)
    password = Column(String(255), nullable=False)
    caregiver = relationship('Caregiver', back_populates='users')

class Caregiver(Base):
    __tablename__ = 'caregiver'
    caregiver_user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    photo = Column(String)  # Assuming photo is stored as a file path or URL
    gender = Column(String(10))
    caregiving_type = Column(String(50))
    hourly_rate = Column(DECIMAL(10, 2), nullable=False)
    users = relationship('Users', back_populates='caregiver')

class Members(Base):
    __tablename__ = 'members'
    member_user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    house_rules = Column(Text)

class Address(Base):
    __tablename__ = 'address'
    member_user_id = Column(Integer, ForeignKey('members.member_user_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    house_number = Column(String(10), nullable=False)
    street = Column(String(255), nullable=False)
    town = Column(String(255), nullable=False)

class Job(Base):
    __tablename__ = 'job'
    job_id = Column(Integer, primary_key=True)
    member_user_id = Column(Integer, ForeignKey('members.member_user_id', ondelete='CASCADE', onupdate='CASCADE'))
    required_caregiving_type = Column(String(255), nullable=False)
    other_requirements = Column(Text)
    date_posted = Column(Date, nullable=False)


class JobApplication(Base):
    __tablename__ = 'job_application'
    caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE'), primary_key=True)
    job_id = Column(Integer, ForeignKey('job.job_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    date_applied = Column(Date, nullable=False)

class Appointment(Base):
    __tablename__ = 'appointment'
    appointment_id = Column(Integer, primary_key=True)
    caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE', onupdate='CASCADE'))
    member_user_id = Column(Integer, ForeignKey('members.member_user_id', ondelete='CASCADE', onupdate='CASCADE'))
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    work_hours = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)

def users_table():
    user_data = [
        {'user_id': 718236, 'email': 'adil_zhalelov@musica36.kz', 'given_name': 'Adil', 'surname': 'Zhalelov', 'city': 'Pavlodar', 'phone_number': '+77777182366', 'profile_description': 'Need care for elderly people.', 'password': 'AgaNu7182'},
        {'user_id': 104236, 'email': 'askha_prince@gmail.com', 'given_name': 'Askhat', 'surname': 'Prince', 'city': 'Almaty', 'phone_number': '+77771021122', 'profile_description': 'Need Care for my child for 2 days.', 'password': 'PustoiKvadrat'},
        {'user_id': 878245, 'email': 'awawa@gmail.com', 'given_name': 'Alice', 'surname': 'Johnson', 'city': 'Astana', 'phone_number': '+77071234578', 'profile_description': 'Need care in special ways.', 'password': 'password123'},
        {'user_id': 485675, 'email': 'daniel.financov@nu.edu.kz', 'given_name': 'Daniel', 'surname': 'Financov', 'city': 'Astana', 'phone_number': '+77079998877', 'profile_description': 'I have 2 dogs and 0 people to looks after them.', 'password': 'secret456'},
        {'user_id': 747848, 'email': 'wyw@gmail.com', 'given_name': 'Charlie', 'surname': 'Williams', 'city': 'Astana', 'phone_number': '+7707771548', 'profile_description': 'Can u look after my house.', 'password': 'pass789'},
        {'user_id': 123484, 'email': 'mlemc@gmail.com', 'given_name': 'David', 'surname': 'Jones', 'city': 'Taldykorgan', 'phone_number': '+77778521456', 'profile_description': 'Need companion care.', 'password': 'secure321'},
        {'user_id': 124785, 'email': 'okokokok@gmail.com', 'given_name': 'Eva', 'surname': 'Ana', 'city': 'Taraz', 'phone_number': '+77021234895', 'profile_description': 'I need physical therapy.', 'password': 'access678'},
        {'user_id': 415754, 'email': 'anadato@gmail.com', 'given_name': 'Frank', 'surname': 'Davis', 'city': 'Astana', 'phone_number': '+77071248954', 'profile_description': 'I need medical care.', 'password': 'private987'},
        {'user_id': 123770, 'email': 'bolat_bolatov@gmail.com', 'given_name': 'Bolat', 'surname': 'Bolatov', 'city': 'Shiely', 'phone_number': '+7778889990', 'profile_description': 'Elderly care need.', 'password': 'classified123'},
        {'user_id': 567423, 'email': 'futurer07@gmail.com', 'given_name': 'Jack', 'surname': 'Sparrow', 'city': 'Astana', 'phone_number': '+77781245874', 'profile_description': 'I own kindergarten, and need workers.', 'password': 'hidden456'},
        #Caregivers:        
        {'user_id': 10, 'email': 'cg1@gmail.com', 'given_name': 'Almat', 'surname': 'Deriev', 'city': 'Astana', 'phone_number': '+77777184366', 'profile_description': 'Prossional of his work.', 'password': '1234'},
        {'user_id': 23, 'email': 'cg2@gmail.com', 'given_name': 'Murat', 'surname': 'Almat', 'city': 'Pavlodar', 'phone_number': '+77771481122', 'profile_description': 'Caregiving expert.', 'password': '1458'},
        {'user_id': 47, 'email': 'cg3@gmail.com', 'given_name': 'Makhambet', 'surname': 'Askar', 'city': 'Almaty', 'phone_number': '+77047234578', 'profile_description': '2 years of experience.', 'password': '2254848452'},
        {'user_id': 78, 'email': 'cg4@gmail.com', 'given_name': 'Maksat', 'surname': 'Arman', 'city': 'Astana', 'phone_number': '+77079492877', 'profile_description': 'I have 10 certificates.', 'password': '484adw8'},
        {'user_id': 11, 'email': 'cg5@gmail.com', 'given_name': 'Marsen', 'surname': 'Musahan', 'city': 'Astana', 'phone_number': '+7704671548', 'profile_description': 'Missian University Bachelor degree of caregiving.', 'password': 'pass7894848'},
        {'user_id': 65, 'email': 'cg6@gmail.com', 'given_name': 'Azat', 'surname': 'Akash', 'city': 'Taraz', 'phone_number': '+77778521486', 'profile_description': 'I am father of 3 children.', 'password': 'secure321'},
        {'user_id': 44, 'email': 'cg7@gmail.com', 'given_name': 'Daiana', 'surname': 'Ana', 'city': 'Shiely', 'phone_number': '+77021236895', 'profile_description': 'Mother of 5 angels.', 'password': '4dw84aw8d4'},
        {'user_id': 14, 'email': 'cg8@gmail.com', 'given_name': 'Dariya', 'surname': 'Aman', 'city': 'Astana', 'phone_number': '+77071295954', 'profile_description': 'I have lots of friends under 10 years.', 'password': '4d84d82a'},
        {'user_id': 29, 'email': 'cg9@gmail.com', 'given_name': 'John', 'surname': 'Bugatti', 'city': 'Taldykorgan', 'phone_number': '+7788489990', 'profile_description': 'Expert in the field currently in.', 'password': 'wwww wwww'},
        {'user_id': 31, 'email': 'cg10@gmail.com', 'given_name': 'Isabella', 'surname': 'Google', 'city': 'Astana', 'phone_number': '+77789945874', 'profile_description': 'Please write any requirements and I will do it!', 'password': '4d8aw4d8___78a!'}
    
    ]
    
    for user_item in user_data:
        session.add(Users(**user_item))

# tables_all()
# users_table()

def caregivers_table():
    caregiver_data = [
        {'caregiver_user_id': 10, 'photo': 'path/to/images1', 'gender': 'Male', 'caregiving_type': 'Elderly Care', 'hourly_rate': 9.00},
        {'caregiver_user_id': 23, 'photo': 'path/to/images2', 'gender': 'Male', 'caregiving_type': 'Child Care', 'hourly_rate': 15.50},
        {'caregiver_user_id': 47, 'photo': 'path/to/images3', 'gender': 'Male', 'caregiving_type': 'Special Needs Care', 'hourly_rate': 18.75},
        {'caregiver_user_id': 78, 'photo': 'path/to/images4', 'gender': 'Male', 'caregiving_type': 'Pet Care', 'hourly_rate': 12.00},
        {'caregiver_user_id': 11, 'photo': 'path/to/images5', 'gender': 'Male', 'caregiving_type': 'Housekeeping', 'hourly_rate': 6.25},
        {'caregiver_user_id': 65, 'photo': 'path/to/images6', 'gender': 'Male', 'caregiving_type': 'Companion Care', 'hourly_rate': 16.00},
        {'caregiver_user_id': 44, 'photo': 'path/to/images7', 'gender': 'Female', 'caregiving_type': 'Physical Therapy', 'hourly_rate': 25.00},
        {'caregiver_user_id': 14, 'photo': 'path/to/images8', 'gender': 'Female', 'caregiving_type': 'Medical Care', 'hourly_rate': 7.50},
        {'caregiver_user_id': 29, 'photo': 'path/to/images9', 'gender': 'Male', 'caregiving_type': 'Elderly Care', 'hourly_rate': 22.50},
        {'caregiver_user_id': 31, 'photo': 'path/to/images10', 'gender': 'FeMale', 'caregiving_type': 'Child Care', 'hourly_rate': 17.00}
    ]
    
    for caregiver_item in caregiver_data:
        session.add(Caregiver(**caregiver_item))

# caregivers_table()

def members_table():
    member_data = [
        {'member_user_id': 718236, 'house_rules': 'No smoking in the house.'},
        {'member_user_id': 104236, 'house_rules': 'Quiet hours after 10 PM.'},
        {'member_user_id': 878245, 'house_rules': 'Allergies: no pets allowed.'},
        {'member_user_id': 485675, 'house_rules': 'Keep common areas clean and tidy.'},
        {'member_user_id': 747848, 'house_rules': 'Respect each other\'s privacy.'},
        {'member_user_id': 123484, 'house_rules': 'Vegetarian household.'},
        {'member_user_id': 124785, 'house_rules': 'Guests allowed with prior notice.'},
        {'member_user_id': 415754, 'house_rules': 'No loud music or parties, no wake up after 7 p.m., no loud speaking, be polite.'},
        {'member_user_id': 123770, 'house_rules': 'Shared grocery expenses.'},
        {'member_user_id': 567423, 'house_rules': 'Weekly cleaning schedule.'}
    ]
    
    for member_item in member_data:
        session.add(Members(**member_item))

# members_table()

def addresses_table():
    address_data = [
        {'member_user_id': 718236, 'house_number': '777', 'street': 'Zharokova', 'town': 'Pavlodar'},
        {'member_user_id': 104236, 'house_number': '012', 'street': 'Turan', 'town': 'Almaty'},
        {'member_user_id': 878245, 'house_number': '125', 'street': 'Makhambet', 'town': 'Astana'},
        {'member_user_id': 485675, 'house_number': '114', 'street': 'Pavel Durov', 'town': 'Astana'},
        {'member_user_id': 747848, 'house_number': '052', 'street': 'Turan', 'town': 'Astana'},
        {'member_user_id': 123484, 'house_number': '071', 'street': 'Tauelsizdik', 'town': 'Taldykorgan'},
        {'member_user_id': 124785, 'house_number': '033', 'street': 'Turan', 'town': 'Taraz'},
        {'member_user_id': 415754, 'house_number': '505', 'street': 'Makhambet', 'town': 'Astana'},
        {'member_user_id': 123770, 'house_number': '457', 'street': 'mcr7', 'town': 'Shiely'},
        {'member_user_id': 567423, 'house_number': '717', 'street': 'Turan', 'town': 'Astana'}
    ]
    
    for address_item in address_data:
        session.add(Address(**address_item))

# addresses_table()

def jobs_table():
    job_data = [
        {'job_id': 0, 'member_user_id': 718236, 'required_caregiving_type': 'Elderly Care', 'other_requirements': 'Experience in similar roles, to be gentle.', 'date_posted': '2023-01-01'},
        {'job_id': 1, 'member_user_id': 104236, 'required_caregiving_type': 'Child Care', 'other_requirements': 'First aid certification required', 'date_posted': '2023-02-01'},
        {'job_id': 2, 'member_user_id': 878245, 'required_caregiving_type': 'Special Needs Care', 'other_requirements': 'Experience with special needs children', 'date_posted': '2023-03-01'},
        {'job_id': 3, 'member_user_id': 485675, 'required_caregiving_type': 'Pet Care', 'other_requirements': 'Comfortable with various pets', 'date_posted': '2023-04-01'},
        {'job_id': 4, 'member_user_id': 747848, 'required_caregiving_type': 'Housekeeping', 'other_requirements': 'gentle', 'date_posted': '2023-05-01'},
        {'job_id': 5, 'member_user_id': 123484, 'required_caregiving_type': 'Companion Care', 'other_requirements': 'Friendly and sociable personality', 'date_posted': '2023-06-01'},
        {'job_id': 6, 'member_user_id': 124785, 'required_caregiving_type': 'Physical Therapy', 'other_requirements': 'To be gentle and certified physical therapist.', 'date_posted': '2023-07-01'},
        {'job_id': 7, 'member_user_id': 415754, 'required_caregiving_type': 'Medical Care', 'other_requirements': 'Medical certification required', 'date_posted': '2023-08-01'},
        {'job_id': 8, 'member_user_id': 123770, 'required_caregiving_type': 'Elderly Care', 'other_requirements': 'Experience in tutoring children', 'date_posted': '2023-09-01'},
        {'job_id': 9, 'member_user_id': 567423, 'required_caregiving_type': 'Child Care', 'other_requirements': 'gentle', 'date_posted': '2023-10-01'}
    ]
    
    for job_item in job_data:
        session.add(Job(**job_item))    

# jobs_table()

def job_applications_table():
    job_application_data = [
        {'caregiver_user_id': 10, 'job_id': 0, 'date_applied': '2023-01-05'},
        {'caregiver_user_id': 23, 'job_id': 1, 'date_applied': '2023-02-10'},
        {'caregiver_user_id': 47, 'job_id': 2, 'date_applied': '2023-03-15'},
        {'caregiver_user_id': 78, 'job_id': 3, 'date_applied': '2023-04-20'},
        {'caregiver_user_id': 11, 'job_id': 4, 'date_applied': '2023-05-25'},
        {'caregiver_user_id': 65, 'job_id': 5, 'date_applied': '2023-06-30'},
        {'caregiver_user_id': 44, 'job_id': 6, 'date_applied': '2023-07-05'},
        {'caregiver_user_id': 14, 'job_id': 7, 'date_applied': '2023-08-10'},
        {'caregiver_user_id': 29, 'job_id': 8, 'date_applied': '2023-09-15'},
        {'caregiver_user_id': 31, 'job_id': 9, 'date_applied': '2023-10-20'}
    ]
    
    for job_application_item in job_application_data:
        session.add(JobApplication(**job_application_item))

# job_applications_table()
 
def appointments_table():
    appointment_data = [
        {'appointment_id': 101, 'caregiver_user_id': 10, 'member_user_id': 718236, 'appointment_date': '2023-01-10', 'appointment_time': '10:00:00', 'work_hours': 4, 'status': 'Accepted'},
        {'appointment_id': 102, 'caregiver_user_id': 23, 'member_user_id': 104236, 'appointment_date': '2023-02-15', 'appointment_time': '15:30:00', 'work_hours': 3, 'status': 'Accepted'},
        {'appointment_id': 112, 'caregiver_user_id': 47, 'member_user_id': 878245, 'appointment_date': '2023-03-20', 'appointment_time': '12:00:00', 'work_hours': 5, 'status': 'Pending'},
        {'appointment_id': 127, 'caregiver_user_id': 78, 'member_user_id': 485675, 'appointment_date': '2023-04-25', 'appointment_time': '08:00:00', 'work_hours': 8, 'status': 'Declined'},
        {'appointment_id': 147, 'caregiver_user_id': 11, 'member_user_id': 747848, 'appointment_date': '2023-05-30', 'appointment_time': '14:45:00', 'work_hours': 6, 'status': 'Accepted'},
        {'appointment_id': 331, 'caregiver_user_id': 65, 'member_user_id': 123484, 'appointment_date': '2023-06-05', 'appointment_time': '18:30:00', 'work_hours': 7, 'status': 'Pending'},
        {'appointment_id': 122, 'caregiver_user_id': 44, 'member_user_id': 124785, 'appointment_date': '2023-07-10', 'appointment_time': '09:15:00', 'work_hours': 4, 'status': 'Accepted'},
        {'appointment_id': 222, 'caregiver_user_id': 14, 'member_user_id': 415754, 'appointment_date': '2023-08-15', 'appointment_time': '11:30:00', 'work_hours': 5, 'status': 'Pending'},
        {'appointment_id': 777, 'caregiver_user_id': 29, 'member_user_id': 123770, 'appointment_date': '2023-09-20', 'appointment_time': '13:45:00', 'work_hours': 6, 'status': 'Declined'},
        {'appointment_id': 179, 'caregiver_user_id': 31, 'member_user_id': 567423, 'appointment_date': '2023-10-25', 'appointment_time': '16:00:00', 'work_hours': 7, 'status': 'Accepted'}
    ]
    
    for appointment_item in appointment_data:
        session.add(Appointment(**appointment_item))

# appointments_table()


# Let's move on to tasks:

# Task #3.1 Update SQL Statement:
updt_num = update(Users).where(and_(Users.given_name == "Adil") , (Users.surname == "Zhalelov")).values(phone_number="+77771010001")
# session.execute(updt_num)


# Task #3.2 Add $0.5 commission fee to the Caregivers’ hourly rate if it's less than $9, or 10% if it's not:
add_half = (
    update(Caregiver).values(hourly_rate=case((Caregiver.hourly_rate < 9, Caregiver.hourly_rate + 0.5), (Caregiver.hourly_rate >= 9, Caregiver.hourly_rate * 1.1), else_=Caregiver.hourly_rate)))
# session.execute(add_half)


# Task 4.1 Delete the jobs by Bolat Bolatov.

# Remove all jobs posted by the specified user
delete_jobs = ( delete(Job).where(Job.member_user_id == Members.member_user_id)
    .where(and_(Members.member_user_id == Users.user_id, Users.given_name == "Bolat", Users.surname == "Bolatov")))

# session.execute(delete_jobs)

# Task 4.2 Delete all members who live on Turan street. 
delete_turan = delete(Members).where(Members.member_user_id == Address.member_user_id).where(Address.street == "Turan")
# session.execute(delete_turan)



#Task 5.1 Select caregiver and member names for the accepted appointments.
# m_alias = aliased(Users)
# c_alias = aliased(Users)
# print("All accepted job appointments:")

# accepted = (session.query(Caregiver.caregiver_user_id,c_alias.given_name.label("caregiver_name"), Members.member_user_id, m_alias.given_name.label("member_name"),)
#     .join(c_alias, Caregiver.caregiver_user_id == c_alias.user_id).join(Appointment, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .join(Members, Members.member_user_id == Appointment.member_user_id).join(m_alias, Members.member_user_id == m_alias.user_id)
#     .filter(Appointment.status == 'Accepted').all()
# )

# i = 0
# for row in accepted:
#     i = i+1
#     print(i, "- "f"Caregiver: {row.caregiver_name}, Member: {row.member_name}")


# Taks 5.2 List job ids that contain ‘gentle’ in their other requirements.
# listing = select(Job.job_id).where(Job.other_requirements == "gentle")
# listing_result = session.execute(listing)
# i = 0

# for row in listing_result:
#     i += 1
#     print(i,"- job id: ",row.job_id)

# TAsk 5.3 List the work hours of Baby Sitter positions.
# select_hours = (select(Appointment.work_hours).join(Job, Appointment.member_user_id == Job.member_user_id).where(Job.required_caregiving_type == "Child Care"))

# res = session.execute(select_hours)

# i = 0
# for row in res:
#     i+=1
#     print(i, "- work hours of baby sitters: ", row.work_hours)


# Task 6.1 Count the number of applicants for each job posted by a member (multiple joins with aggregation)
# num_applicants = (session.query(Job.job_id, func.count(JobApplication.caregiver_user_id).label('num_applicants')).join(JobApplication, Job.job_id == JobApplication.job_id).group_by(Job.job_id).all())

# n = len(num_applicants)
# print(f"Applicants number: {n}")


#Task 6.2: Total hours spent by care givers for all accepted appointments (multiple joins with aggregation)
# thours = session.query(func.sum(Appointment.work_hours))\
#     .join(Caregiver).filter(Appointment.status == 'Accepted').scalar()

# print(f'Total hours spent by caregivers: {thours}')


# Task 6.3:  Average pay of caregivers based on accepted appointments
# av_pay = session.query(func.avg(Caregiver.hourly_rate * Appointment.work_hours)).join(Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id).\
#     filter(Appointment.status == 'Accepted').group_by(Caregiver.caregiver_user_id).all()

# total_pay = 0
# for payment in av_pay:
#     total_pay += payment[0]
# if(len(av_pay) != 0):
#     average_pay = total_pay / len(av_pay)
#     print(f"Average pay of caregivers: {average_pay}")
# else:
#     print('Invalid case!')


# Task: 6.4 Caregivers who earn above average based on accepted appointments
# aboveAv = session.query(Caregiver).join(Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id).filter(Appointment.status == 'Accepted')\
#     .group_by(Caregiver.caregiver_user_id).having(func.avg(Caregiver.hourly_rate * Appointment.work_hours) > average_pay).all()

# print('\nCaregivers who earn above average based on accepted appointments')

# for caregiver in aboveAv:
#     print(f"Caregiver_id: {caregiver.caregiver_user_id} & caregiver_name: {caregiver.users.given_name} {caregiver.users.surname}")


# Task 7: Calculate the total cost to pay for a caregiver for all accepted appointments
# total = session.query(func.sum(Caregiver.hourly_rate * Appointment.work_hours)).join(Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id).filter(Appointment.status == 'Accepted').scalar()

# print(f"Calculated total cost to pay for a caregiver: {total}")


# Task 8: View all job applications and the applicants
# res = (
#     session.query(JobApplication.job_id, JobApplication.caregiver_user_id, Users.given_name.label('caregiver_given_name'),
#         Users.surname.label('caregiver_surname'), Job.required_caregiving_type,
#         Members.member_user_id, Users.given_name.label('member_given_name'), Users.surname.label('member_surname'))
#     .join(Caregiver, JobApplication.caregiver_user_id == Caregiver.caregiver_user_id)
#     .join(Users, Caregiver.caregiver_user_id == Users.user_id)
#     .join(Job, JobApplication.job_id == Job.job_id)
#     .join(Members, Job.member_user_id == Members.member_user_id)
# )

# final = res.all()

# for row in final:
#     print(row)

# The end!

session.commit()

