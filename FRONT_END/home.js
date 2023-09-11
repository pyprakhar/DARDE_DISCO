window.addEventListener('scroll',function(){
    const header = document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY > 0);
});

function togglemenu(){
    const menutoggle = document.querySelector('.menutoggle');
    const navigation = document.querySelector('.navigation');
    menutoggle.classList.toggle('active');
    navigation.classList.toggle('active');
};

function navigateTo(page) {
    switch (page) {
        case 'signup':
            window.location.href = 'front end/signup_student.html';
            break;
        case 'mentor':
            window.location.href = 'front end/mentors.html';
            break;
    }
}

        
    
