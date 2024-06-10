

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

    // Cambiar automáticamente cada 5 segundos (5000 milisegundos)
    setInterval(nextSlide, 5000);
});


document.addEventListener("DOMContentLoaded", function() {
    const professionalLinks = document.querySelectorAll(".professional-link");
    const additionalInfo = document.getElementById("additional-info");

    professionalLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Evita que el enlace cambie de página
            
            // Oculta los otros barberos
            document.querySelectorAll(".image-with-text").forEach(function(barbero) {
                if (barbero.id !== link.parentNode.id) {
                    barbero.style.display = "none";
                }
            });
            
            // Muestra la información adicional
            additionalInfo.style.display = "block";
        });
    });
});
var nombreBarbero = ""; // Variable global para almacenar el nombre del barbero seleccionado
$(".professional-link").click(function() {
    nombreBarbero = $(this).find("img").data("barbero");
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






    // Espera a que el DOM esté completamente cargado
// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Variable global para almacenar el nombre del barbero seleccionado
    var nombreBarbero = "";

    // Captura el nombre del barbero seleccionado cuando se hace clic en un enlace de barbero.
    $(".professional-link").click(function() {
        nombreBarbero = $(this).find("img").data("barbero");
        localStorage.setItem("selectedBarber", nombreBarbero); // Guarda el nombre del barbero en el almacenamiento local
    });

    // Al hacer clic en el botón de confirmar y agendar, redirige a la siguiente página
    
});



var nombreBarbero = localStorage.getItem("selectedBarber");
        if (nombreBarbero) {
            // Muestra el nombre del barbero
            document.getElementById("nombre-barbero").textContent = nombreBarbero;
            // Puedes cambiar la ruta de la imagen según el nombre del barbero seleccionado
            document.getElementById("barbero-seleccionado").querySelector("img").src = "../assets/" + "barber" + nombreBarbero + ".jpg";
        }


        
        
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
        
            // Cambiar automáticamente cada 5 segundos (5000 milisegundos)
            setInterval(nextSlide, 5000);
        
            // Captura el nombre del barbero seleccionado cuando se hace clic en un enlace de barbero.
            var nombreBarbero = "";
            $(".professional-link").click(function() {
                nombreBarbero = $(this).find("img").data("barbero");
                localStorage.setItem("selectedBarber", nombreBarbero); // Guarda el nombre del barbero en el almacenamiento local
            });
        
            // Al hacer clic en el botón de confirmar y agendar, redirige a la siguiente página
            
        
    // Código para el calendario
            var calendarEl = document.getElementById('calendario');
            var calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'timeGridWeek', // Vista inicial del calendario en semanal
                locale: 'es', // Establece el idioma en español
                slotMinTime: '10:00:00', // Hora mínima visible
                slotMaxTime: '18:00:00', // Hora máxima visible
                selectable: true, // Habilita la selección de fechas
                select: function(info) {
                    // Abrir el modal al seleccionar una fecha y hora
                    openModal(info.start, info.end);
                },
                eventClick: function(info) {
                    // Esta función se llama cuando se hace clic en un evento
                    var eventTitle = info.event.title; // Obtiene el título del evento
                    var startDate = info.event.start; // Obtiene la fecha y hora de inicio del evento
                    var endDate = info.event.end; // Obtiene la fecha y hora de finalización del evento
                    console.log("Evento seleccionado:", eventTitle);
                    console.log("Fecha de inicio del evento:", startDate);
                    console.log("Fecha de finalización del evento:", endDate);
        
                    // Guardar la hora seleccionada (aquí puedes añadir tu lógica para guardar la hora)
                    // Ejemplo:
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
            calendar.render(); // Renderiza el calendario
        git a
            function generateEvents(timeSlots, eventTitle) {
                const events = [];
                const start = new Date();
                const end = new Date();
                end.setDate(start.getDate() + 21); // Tres semanas desde hoy
        
                for (let date = new Date(start); date <= end; date.setDate(date.getDate() + 1)) {
                    if (date.getDay() >= 1 && date.getDay() <= 6) { // De lunes a sábado
                        const eventDate = date.toISOString().split('T')[0];
                        // Eventos para la vista semanal y diaria
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
                // Obtén las referencias a los elementos del modal
                var modal = document.getElementById('confirmModal');
                var startDateElement = document.getElementById('selectedStartDate');
                var endDateElement = document.getElementById('selectedEndDate');
                var confirmButton = document.getElementById('confirmButton');
            
                // Asigna la fecha y hora seleccionada a los elementos del modal
                startDateElement.textContent = startDate.toLocaleString();
                endDateElement.textContent = endDate.toLocaleString();
            
                // Abre el modal
                $(modal).modal('show');
            
                // Agrega un evento al botón "Confirmar" para redirigir a la siguiente página
                confirmButton.addEventListener('click', function() {
                    // Aquí puedes implementar la lógica para redirigir a la siguiente página
                    // Por ejemplo:
                     window.location.href = '../home/contactForm.html';
                    // Asegúrate de ajustar la URL según tu estructura de archivos.
                });
            }
            
            
        });