from odoo import http
from odoo.http import request
from odoo.exceptions import UserError

class CustomWebsite(http.Controller):
    
    
    @http.route('/helpdesk/ticket', type='http', auth='public', website=True)
    def my_custom_page(self, **kwargs):  
        
        return http.request.render('webpage.template_name', {})
    
    
    @http.route('/abcde', type='http', auth='public', csrf=True, website=True)
    def create_ticket(self, **post):
        raise UserError("ABcksd")
        
        project_id = post.get('project')
        subject_id = post.get('subject')
        category_id = post.get('category')
        sub_category_id = post.get('sub_category')
        priority = post.get('priority')
        partner_id = post.get('name')
        email = post.get('email')
        description = post.get('description')
        # attachment = request.httprequest.files.get('attachment')  # File upload

        print(f"Description: {description}", flush=True)
        # Create a new record in sh.helpdesk.ticket
        ticket_vals = {
            'project_id': project_id,
            'subject_id': subject_id,
            'category_id': category_id,
            'sub_category_id': sub_category_id,
            'priority': priority,
            'partner_id': partner_id,
            'email': email,
            'description': description,
        }
        new_ticket = request.env['sh.helpdesk.ticket'].sudo().create(ticket_vals)

        # Handle file attachment (optional)
        # if attachment:
        #     attachment_data = {
        #         'name': attachment.filename,
        #         'res_model': 'sh.helpdesk.ticket',
        #         'res_id': new_ticket.id,
        #         'type': 'binary',
        #         'datas': attachment.read().encode('base64'),
        #         'mimetype': attachment.content_type,
        #     }
        #     request.env['ir.attachment'].sudo().create(attachment_data)

        # Redirect or display success message
        return request.render('webpage.success_page_template', {'ticket_id': new_ticket.id})
