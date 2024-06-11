document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll(".carousel-slide");
    let currentSlide = 0;

    function showSlide(slideIndex) {
        slides.forEach(function(slide) {
            slide.classList.remove("active");
        });
        slides[slideIndex].classList.add("active");
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }

    const prevButton = document.querySelector(".prev-slide");
    const nextButton = document.querySelector(".next-slide");

    prevButton.addEventListener("click", prevSlide);
    nextButton.addEventListener("click", nextSlide);

    setInterval(nextSlide, 5000);

    const professionalLinks = document.querySelectorAll(".professional-link");
    const additionalInfo = document.getElementById("additional-info");
    let nombreBarbero = "";

    professionalLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            document.querySelectorAll(".image-with-text").forEach(function(barbero) {
                if (barbero.id !== link.parentNode.id) {
                    barbero.style.display = "none";
                } else {
                    link.classList.add("disabled-link");
                }
            });
            additionalInfo.style.display = "block";
            nombreBarbero = link.querySelector("img").getAttribute("data-barbero");
            localStorage.setItem("selectedBarber", nombreBarbero);
        });
    });

    $(document).ready(function(){
        $(".agregar-servicio").click(function(){
            var nombreServicio = $(this).data('nombre');
            var valorServicio = $(this).data('valor');

            $("#nombreBarbero").text("Profesional: " + nombreBarbero);
            $("#nombreServicio").text("Servicio: " + nombreServicio);
            $("#valorServicio").text("Valor: " + valorServicio);

            $("#servicioModal").modal('show');
        });
    });

    $("#confirmar-agendar").click(function() {
        $("#servicioModal").modal('hide');
        document.getElementById("additional-info").style.display = "none";
        document.getElementById("fecha-hora-section").style.display = "block";
        var nombreBarbero = localStorage.getItem("selectedBarber");
        if (nombreBarbero) {
            document.getElementById("nombre-barbero").textContent = nombreBarbero;
            document.getElementById("barbero-seleccionado").querySelector("img").src = "{% static 'barber" + nombreBarbero + ".jpg' %}";
        }
        initCalendar();
    });

    function initCalendar() {
        var calendarEl = document.getElementById('calendario');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'timeGridWeek',
            locale: 'es',
            slotMinTime: '10:00:00',
            slotMaxTime: '18:00:00',
            selectable: true,
            select: function(info) {
                openModal(info.start, info.end);
            },
            eventClick: function(info) {
                var eventTitle = info.event.title;
                var startDate = info.event.start;
                var endDate = info.event.end;
                openModal(startDate, endDate);
            },
            events: generateEvents([
                { startHour: '10:00', endHour: '10:30' },
                { startHour: '10:30', endHour: '11:00' },
                { startHour: '11:00', endHour: '11:30' },
                { startHour: '11:30', endHour: '12:00' },
                { startHour: '13:00', endHour: '13:30' },
                { startHour: '13:30', endHour: '14:00' },
                { startHour: '14:00', endHour: '14:30' },
                { startHour: '14:30', endHour: '15:00' },
                { startHour: '15:00', endHour: '15:30' },
                { startHour: '15:30', endHour: '16:00' },
                { startHour: '16:00', endHour: '16:30' },
                { startHour: '16:30', endHour: '17:00' }
            ], 'disponible')
        });
        calendar.render();
    }

    function generateEvents(timeSlots, eventTitle) {
        const events = [];
        const start = new Date();
        const end = new Date();
        end.setDate(start.getDate() + 21);

        for (let date = new Date(start); date <= end; date.setDate(date.getDate() + 1)) {
            if (date.getDay() >= 1 && date.getDay() <= 6) {
                const eventDate = date.toISOString().split('T')[0];
                timeSlots.forEach(slot => {
                    events.push({
                        title: eventTitle,
                        start: `${eventDate}T${slot.startHour}:00`,
                        end: `${eventDate}T${slot.endHour}:00`,
                        display: 'auto'
                    });
                });
            }
        }
        return events;
    }

    function openModal(startDate, endDate) {
        var modal = document.getElementById('confirmModal');
        var startDateElement = document.getElementById('selectedStartDate');
        var endDateElement = document.getElementById('selectedEndDate');
        var confirmButton = document.getElementById('confirmButton');

        startDateElement.textContent = startDate.toLocaleString();
        endDateElement.textContent = endDate.toLocaleString();

        $(modal).modal('show');

        confirmButton.addEventListener('click', function() {
            $(modal).modal('hide');
            document.getElementById("fecha-hora-section").style.display = "none";
            document.getElementById("form-container").style.display = "block";
        });
    }
});

document.getElementById('ReservaForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const email = document.getElementById('email').value;
    const telefono = document.getElementById('telefono').value;
    const edad = document.getElementById('edad').value;
    const observaciones = document.getElementById('observaciones').value;
    const profesional = localStorage.getItem('selectedBarber');
    const servicio = document.getElementById('nombreServicio').textContent.replace('Servicio: ', '');
    const fecha = document.getElementById('selectedStartDate').textContent;
    const hora = document.getElementById('selectedEndDate').textContent;

    fetch('/reservar/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            nombre: nombre,
            apellido: apellido,
            email: email,
            telefono: telefono,
            edad: edad,
            observaciones: observaciones,
            profesional: profesional,
            servicio: servicio,
            fecha: fecha,
            hora: hora
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Reserva realizada con éxito. Revisa tu correo para los detalles.');
            // Aquí puedes redirigir al usuario o mostrar un mensaje de éxito
        } else {
            alert('Hubo un error al realizar la reserva. Inténtalo de nuevo.');
        }
    });
});


