    $(function () {
       $("#id_password1, #id_password2, #id_username").addClass("form-control").addClass("form-singin");
       $("#id_username").attr("placeholder","Логин");
       $("#id_password1").attr("placeholder","Пароль");
       $("#id_password2").attr("placeholder","Подтверждение пароля");


       $("#id_previous_place, #id_previous_position, #id_education_name, #id_education_speciality").addClass("form-control").addClass("form-singin");
       $("#id_previous_place").attr("placeholder","Место работы").attr("required","required");
       $("#id_previous_position").attr("placeholder","Должность").attr("required","required");
       $("#id_education_name").attr("placeholder","Место учебы").attr("required","required");
       $("#id_education_speciality").attr("placeholder","Специальность").attr("required","required");

       $(".someactive").click(function(){

           // $(".someactive").removeClass("active");
            $(this).addClass("active");

       });

    });