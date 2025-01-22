odoo.define('sh_all_in_one_helpdesk.CreateTicketPopup', function (require) {
    'use strict';


    var publicWidget = require('web.public.widget');

    publicWidget.registry.CreateTicketPopup = publicWidget.Widget.extend({
        selector: '#createticketModal',


        events: {
            'change #portal_file': '_onChangePortalFile',
            'click #partner': '_onClickPartner',
            'click #portal_category': '_onClickPortalCategory',
            'click #portal_team': '_onClickPortalTeam',
            'click #create_sh_helpdesk_ticket': '_onClickCreateTicket', //Yaminah
        },


        /**
         * @override
         */
        start: function () {
            var def = this._super.apply(this, arguments);
            var self = this
            $('#portal_assign_multi_user').select2();

            $.ajax({
                url: "/portal-subcategory-data",
                data: { category_id: $("#portal_category").val() },
                type: "post",
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#portal_subcategory > option").remove();
                    $("#portal_subcategory").append('<option value="' + "sub_category" + '">' + "Select Sub Category" + "</option>");
                    _.each(datas.sub_categories, function (data) {
                        $("#portal_subcategory").append('<option value="' + data.id + '">' + data.name + "</option>");
                    });
                },
            });


            $.ajax({
                url: "/portal-partner-data",
                data: {},
                type: "post",
                async: false,
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#partner_ids > option").remove();
                    _.each(datas.partners, function (data) {
                        $("#partner_ids").append('<option data-id="' + data.id + '" value="' + data.name + '">');
                    });
                },
            });


            $.ajax({
                url: "/portal-subcategory-data",
                data: { category_id: $("#portal_category").val() },
                type: "post",
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#portal_subcategory > option").remove();
                    $("#portal_subcategory").append('<option value="' + "sub_category" + '">' + "Select Sub Category" + "</option>");
                    _.each(datas.sub_categories, function (data) {
                        $("#portal_subcategory").append('<option value="' + data.id + '">' + data.name + "</option>");
                    });
                },
            });

            $.ajax({
                url: "/portal-user-data",
                data: { team_id: $("#portal_team").val() },
                type: "post",
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#portal_assign_user > option").remove();
                    $("#portal_assign_user").append('<option value="' + "user" + '">' + "Select Assign User" + "</option>");
                    $("#portal_assign_multi_user").select2('destroy');
                    $("#portal_assign_multi_user > option").remove();
                    $("#portal_assign_multi_user").append('<option value="' + "users" + '">' + "Select Multi Users" + "</option>");
                    _.each(datas.users, function (data) {
                        $("#portal_assign_user").append('<option value="' + data.id + '">' + data.name + "</option>");
                        $("#portal_assign_multi_user").append('<option value="' + data.id + '">' + data.name + "</option>");
                    });
                    $("#portal_assign_multi_user").select2();
                },
            });


            $('body').find('#new_request').on("click", self._onClickNewRequest.bind(self));
            return def
        },


        _onChangePortalFile: function (ev) {

            var input = document.getElementById('portal_file');
            var file = input.files;
            var total_file_size = 0.0

            for (let index = 0; index < file.length; index++) {
                const element = file[index];
                total_file_size = total_file_size + element.size
            }

            if (total_file_size / 1024 > $('#sh_file_size').val()) {
                alert("Attached file exceeds the " + String($('#sh_file_size').val()) + "KB file size limit");
                $("#portal_file").val("");
            }
        },

        _onClickNewRequest: function (ev) {
            $("#createticketModal").modal("show");
        },

        _onClickPortalCategory: function (ev) {
            $.ajax({
                url: "/portal-subcategory-data",
                data: { category_id: $("#portal_category").val() },
                type: "post",
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#portal_subcategory > option").remove();
                    $("#portal_subcategory").append('<option value="' + "sub_category" + '">' + "Select Sub Category" + "</option>");
                    _.each(datas.sub_categories, function (data) {
                        $("#portal_subcategory").append('<option value="' + data.id + '">' + data.name + "</option>");
                    });
                },
            });
        },

        _onClickPartner: function (ev) {
            var option = $("#partner_ids").find("[value='" + $("#partner").val() + "']");
            var partner = option.data("id");
            $("#partner_id").val("");
            $("#partner_id").val(partner);
            if ($("#partner_id").val() != "") {
                $.ajax({
                    url: "/selected-partner-data",
                    data: { partner_id: $("#partner_id").val() },
                    type: "post",
                    cache: false,
                    success: function (result) {
                        var datas = JSON.parse(result);
                        $("#portal_contact_name").val(datas.name);
                        $("#portal_email").val(datas.email);
                    },
                });
            } else {
                $("#portal_contact_name").val("");
                $("#portal_email").val("");
            }
        },

        _onClickPortalTeam: function (ev) {
            $.ajax({
                url: "/portal-user-data",
                data: { team_id: $("#portal_team").val() },
                type: "post",
                cache: false,
                success: function (result) {
                    var datas = JSON.parse(result);
                    $("#portal_assign_user > option").remove();
                    $("#portal_assign_multi_user").select2('destroy');
                    $("#portal_assign_multi_user > option").remove();
                    $("#portal_assign_user").append('<option value="' + "user" + '">' + "Select Assign User" + "</option>");
                    $("#portal_assign_multi_user").append('<option value="' + "users" + '">' + "Select Multi Users" + "</option>");
                    _.each(datas.users, function (data) {
                        $("#portal_assign_user").append('<option value="' + data.id + '">' + data.name + "</option>");
                        $("#portal_assign_multi_user").append('<option value="' + data.id + '">' + data.name + "</option>");
                    });
                    $("#portal_assign_multi_user").select2();
                },
            });
        },
        // Yaminah
        _onClickCreateTicket: function(ev){
            ev.preventDefault();  // Prevent the default form submission
            let category = $("#portal_category").find(":selected").text()
            if(category == 'Select Category'){
                alert('Please select a category')
                return
            }
            let subject = $("#portal_subject").find(":selected").text()
            if(subject == 'Select Subject'){
                alert('Please select a Subject')
                return
            }
            let sub_category = $("#portal_subcategory").find(":selected").text()
            if(sub_category == 'Select Sub Category'){
                alert('Please select a Sub Category')
                return
            }
            let portal_priority = $("#portal_priority").find(":selected").text()
            if(portal_priority == 'Select Priority'){
                alert('Please select a Priority')
                return
            }
            let portal_project = $("#portal_project").find(":selected").text()
            if(portal_project == 'Select Project'){
                alert('Please select a Project')
                return
            }
            let portal_contact_name = $("#portal_contact_name").val()
            if(portal_contact_name == ''){
                alert('Please Enter a Name')
                return
            }
            let portal_email = $("#portal_email").val()
            if(portal_email == ''){
                alert('Please Enter an Email')
                return
            }
            let portal_description = $("#description").val()
            if(portal_description == ''){
                alert('Please Enter a Description')
                return
            }
            $("#form_id").submit();
        }
        // Yaminah
    });
});
