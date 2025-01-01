from odoo import models, api, fields

#Demo Task 01: In the quotation view of sale module, whenever the user edits the analytic distribution field, 
# then it must be changed in the invoice either if the invoice is generated or not.
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #Overiding the default write method which trigger when try to edit the record in the selected model  
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        
        if 'order_line' in vals: 
        #If any field value is changed in the sale.order.line model 
        # then there will be order_line in the vals 
            
            for order in self:
                
                for line in order.order_line:
                    
                    if line.analytic_distribution:  
                    #If the analytic_distribution is updated then line is having a key of that and 
                    # it will be called as an attribute
                        
                        invoices = order.invoice_ids 
                        #this will bring the invoices associated with quotation which is just updated 
                        # because the invoice_ids is one2many field connect with account.move model
                        # filtered(lambda inv: inv.state != 'cancel') can also apply this attribute with the 
                        # above line to just get the invoices whose state are not cancelled
                        
                        for invoice in invoices:
                        # accessing a single invoice from invoices because there may be multiple invoices
                        # and through this can also access attributes like invoice.product_id.name
                            
                            for invoice_line in invoice.invoice_line_ids:
                            # accessing the account the fields of account.move.line model through the invoice_line_ids
                            # and can write in the account.move.line fields
                                
                                if invoice_line.product_id == line.product_id:
                                # accessing the same product from quotation to invoice through product_id

                                    invoice_line.write({'analytic_distribution': line.analytic_distribution})
                                    
        return res