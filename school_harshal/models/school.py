from odoo import models,fields


class School(models.Model):
    _name = "school.school"
    _description = "school_management_system"
    school_id=fields.Integer(string="school id")
    name=fields.Char(string="name")
    # student_id=fields.Many2one('school.student',name="student")
    teacher_ids=fields.One2many('school.teacher','school_id',string='teachers')


class Student(models.Model):
    _name = "school.student"
    _description = "this is student model"

    stud_id=fields.Integer(string="number")
    name=fields.Char(string="name")
    age=fields.Integer(string='Age')
    gender=fields.Selection([(1,'male'),(2,'female'),(3,'transgender')],default=1)
    photo=fields.Binary(string="photo")
    school_id=fields.Many2one('school.school',string='school id')
    teacher_ids=fields.Many2many('school.teacher','student_teacher_relation_table','teach_id','stud_id')


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "this is teacher model"

    teach_id=fields.Integer(string="number")
    name=fields.Char(string="name")
    age=fields.Integer(string='Age')
    gender=fields.Selection([(1,'male'),(2,'female'),(3,'transgender')],default=1)
    photo=fields.Binary(string="photo")
    school_id=fields.Many2one('school.school',string="school id")