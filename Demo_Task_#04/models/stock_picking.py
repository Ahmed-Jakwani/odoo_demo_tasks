from odoo import models, api, fields

# Demo Task : In the receipts of stock.picking model, if the value of Quantity (quantity) is greater then Demand (product_uom_qty), 
# then hide the validate button and add a new Request for Approval button,
# when the user hits on Request for Approval, then Approve/Reject buttons are visible to a specific user,
# if the user Approves, then Validate button becomes visible to all the users and the columns demand and done become readonly,
# and if the user rejects, then again Request for Approval becomes visible.

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    #if true (Validate), if false (Request for Approval)
    validate_rfa_button = fields.Boolean(string="Show Validate Button", compute="_compute_validate_rfa_button")
    
    # if false (Request for Approval) becomes invisible
    hide_rfa_button = fields.Boolean(string="Hide RFA Button")
    
    # if True, then Approve/Reject buttons becomes visible, if false then not.
    approve_reject_button = fields.Boolean(string="Show Approve Reject Button")

    # if True, then Demand and Quantity fields becomes read-only, if false then not
    static_qty = fields.Boolean(string="Static Quantity")


    # Computing the validate and RFA button on change of Demand and Quantity
    @api.depends('move_ids_without_package.quantity')
    def _compute_validate_rfa_button(self):
        
        # Initially assign a value to the validate button
        self.validate_rfa_button = True
        
        for record in self:

            for move in record.move_ids_without_package:
                
                # if the value of done is larger then demand
                if (move.quantity > move.product_uom_qty):
                    
                    if (self.static_qty == False):
                        
                        self.validate_rfa_button = False

                        break
                
                # if the value of done is not larger then demand
                else:
                    
                    # Validate button becomes visible
                    self.validate_rfa_button = True
                    
                    # Approve/Reject will not be visible
                    self.approve_reject_button = False
                    
                    # RFA button will not be visible
                    self.hide_rfa_button = False

                    self.static_qty = False

                    
                    
                    
    # Method will be called for clicking on RFA button  
    def action_request_for_approval(self):
        
        # If the Approve/Reject buttons are not visible and RFA buttons is visible
        if self.approve_reject_button == False:
            
            # Approve/Reject will become visible
            self.approve_reject_button = True
            
            # RFA button will not be visible means "Request has sent"
            self.hide_rfa_button = True
    
    
    # Method will be called for clicking on Approve button  
    def action_approve(self):
        
        # If Validate & RFA both buttons are not visible (means the request is in Approval stage)
        if self.validate_rfa_button == False and self.hide_rfa_button == True:
            
            # Validate button becomes visible
            self.validate_rfa_button = True
            
            # Make the Demand the Done column for read-only
            self.static_qty = True

            # Approve/Reject will become invisible
            self.approve_reject_button = False
            
            self.hide_rfa_button = False
      
      
    # Method will be called for clicking on Reject button      
    def action_reject(self):
        
        # If Validate & RFA both buttons are not visible (means the request is in Approval stage)
        if self.validate_rfa_button == False and self.hide_rfa_button == True:
            
            # Make the RFA button visible again (because this request is rejected)
            self.hide_rfa_button = False
            
            # Hide the Approve and Reject buttons
            self.approve_reject_button = False