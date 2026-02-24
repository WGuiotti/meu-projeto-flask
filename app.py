# Import necessary modules from Flask
from flask import Flask, render_template, request
import os

# Initialize the Flask application
app = Flask(__name__)

# Professional Configuration: Define path to database
app.config['DATABASE'] = os.path.join(app.root_path, 'database', 'site.db')

# Translations Dictionary
translations = {
    'pt': {
        'title': 'GuIIOTTI - Soluções em IIoT & Automação',
        'btn_about': 'Sobre Nós',
        'hero_h1': 'Inovando o Futuro',
        'hero_p': 'Conectando Casas, Edifícios e Indústrias através de IIoT avançada, Automação e Engenharia Elétrica.',
        'garage_h2': 'Garagem Inteligente',
        'garage_p': 'Nunca mais esqueça seu portão aberto além de ganhar tempo no seu dia a dia!',
        'garage_alt': 'Controle de portão de garagem inteligente via aplicativo',
        'btn_services': 'Nossos Serviços',
        'section_services': 'O Que Fazemos',
        'card1_title': 'Soluções IIoT',
        'card1_p': 'Transformando indústrias com insights baseados em dados. Implementamos estratégias de Internet Industrial das Coisas para monitorar, analisar e otimizar operações em tempo real.',
        'card2_title': 'Automação IoT',
        'card2_p': 'Ambientes de vida e trabalho inteligentes. Do controle residencial inteligente a sistemas complexos de gestão predial, damos vida à automação.',
        'card3_title': 'Serviços Elétricos',
        'card3_p': 'Infraestrutura de energia confiável. Fornecemos instalação elétrica de alta qualidade, manutenção e consultoria para projetos residenciais e industriais.',
        'section_sectors': 'Setores que Atendemos',
        'tag1': 'Casas Inteligentes',
        'tag2': 'Edifícios Comerciais',
        'tag3': 'Indústrias Modernas',
        'footer': '© 2024 GuIIOTTI. Todos os direitos reservados.',
        'about_title': 'Sobre Nossa Missão',
        'about_p': 'Dedicamo-nos a preencher a lacuna entre a engenharia elétrica tradicional e as modernas soluções de IoT.'
    },
    'en': {
        'title': 'GuIIOTTI - IIoT & Automation Solutions',
        'btn_about': 'About Us',
        'hero_h1': 'Innovating the Future',
        'hero_p': 'Connecting Homes, Buildings, and Industries through advanced IIoT, Automation, and Electrical Engineering.',
        'garage_h2': 'Smart Garage',
        'garage_p': 'Never forget your gate open again and save time in your daily life!',
        'garage_alt': 'Smart garage gate control via app',
        'btn_services': 'Our Services',
        'section_services': 'What We Do',
        'card1_title': 'IIoT Solutions',
        'card1_p': 'Transforming industries with data-driven insights. We implement Industrial Internet of Things strategies to monitor, analyze, and optimize operations in real-time.',
        'card2_title': 'IoT Automation',
        'card2_p': 'Smart living and working environments. From intelligent home control to complex building management systems, we bring automation to life.',
        'card3_title': 'Electrical Services',
        'card3_p': 'Reliable power infrastructure. We provide high-quality electrical installation, maintenance, and consulting for residential and industrial projects.',
        'section_sectors': 'Sectors We Serve',
        'tag1': 'Smart Homes',
        'tag2': 'Commercial Buildings',
        'tag3': 'Modern Industries',
        'footer': '© 2024 GuIIOTTI. All rights reserved.',
        'about_title': 'About Our Mission',
        'about_p': 'We are dedicated to bridging the gap between traditional electrical engineering and modern IoT solutions.'
    },
    'es': {
        'title': 'GuIIOTTI - Soluciones IIoT y Automatización',
        'btn_about': 'Sobre Nosotros',
        'hero_h1': 'Innovando el Futuro',
        'hero_p': 'Conectando Hogares, Edificios e Industrias a través de IIoT avanzada, Automatización e Ingeniería Eléctrica.',
        'garage_h2': 'Garaje Inteligente',
        'garage_p': '¡Nunca más olvides tu portón abierto y ahorra tiempo en tu día a día!',
        'garage_alt': 'Control de portón de garaje inteligente vía app',
        'btn_services': 'Nuestros Servicios',
        'section_services': 'Lo Que Hacemos',
        'card1_title': 'Soluciones IIoT',
        'card1_p': 'Transformando industrias con información basada en datos. Implementamos estrategias de Internet Industrial de las Cosas para monitorear, analizar y optimizar operaciones en tiempo real.',
        'card2_title': 'Automatización IoT',
        'card2_p': 'Entornos de vida y trabajo inteligentes. Desde el control inteligente del hogar hasta complejos sistemas de gestión de edificios, damos vida a la automatización.',
        'card3_title': 'Servicios Eléctricos',
        'card3_p': 'Infraestructura eléctrica confiable. Ofrecemos instalación eléctrica de alta calidad, mantenimiento y consultoría para proyectos residenciales e industriales.',
        'section_sectors': 'Sectores que Servimos',
        'tag1': 'Hogares Inteligentes',
        'tag2': 'Edificios Comerciales',
        'tag3': 'Industrias Modernas',
        'footer': '© 2024 GuIIOTTI. Todos los derechos reservados.',
        'about_title': 'Sobre Nuestra Misión',
        'about_p': 'Nos dedicamos a cerrar la brecha entre la ingeniería eléctrica tradicional y las soluciones modernas de IoT.'
    }
}

# Define the route for the root URL ('/')
@app.route('/')
def index():
    # Get language from query parameters, default to 'pt'
    lang = request.args.get('lang', 'pt')
    if lang not in translations:
        lang = 'pt'
    # Render the index.html template
    return render_template('index.html', text=translations[lang], lang=lang)

# Example route for a sub-page in the 'pages' folder
@app.route('/about')
def about():
    lang = request.args.get('lang', 'pt')
    if lang not in translations:
        lang = 'pt'
    return render_template('pages/about.html', text=translations[lang], lang=lang)

# Run the application if executed as the main script
if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True)