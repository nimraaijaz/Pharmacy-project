document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("form").addEventListener("submit", function (event) { 
                var email = document.getElementById('email').value;
                var pass = document.getElementById('password').value;
                var checkbox = document.getElementById('checkbox').checked ? 'yes' : 'no';
                passRegex = /^[\dA-Za-z\W]+$/;
                emailRegex = /^[\dA-Za-z]+@[A-Za-z]+\.[A-Za-z]+$/;
                if (pass == '' || email == '' || !passRegex.test(pass) || !emailRegex.test(email)) {
                        alert('please fill the data with valid field');
                    } else {
                        alert('\nPassword:' + pass + '\nEmail:' + email +'\nDo You Agree:' + checkbox);
                    }
                });
        })