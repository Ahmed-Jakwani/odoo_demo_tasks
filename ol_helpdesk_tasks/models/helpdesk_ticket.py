from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError

class HelpdeskInherit(models.Model):
    _inherit='sh.helpdesk.ticket'
    
    tasks_count= fields.Integer(string='Tasks',compute="compute_tasks_count")
    project_id= fields.Many2one('project.project',string='Project')
    
    def create_task(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'form',
            'view_id': self.env.ref('project.view_task_form2').id,
            'target': 'new',
            'context': {
                'default_project_id': self.project_id.id,
                'default_name': self.name,
                'default_description': self.description,
                'default_sh_ticket_ids': [(4,self.id)],
            }
        }
        
    def compute_tasks_count(self):
        for record in self:
            record.tasks_count = self.env['project.task'].search_count(
                [('sh_ticket_ids','in',[self.id])]
            ) 

        
    def get_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'tree,form',
            'res_model': 'project.task',
            'domain': [('sh_ticket_ids','in',[self.id])],
            'context': {'create': False}
        }

