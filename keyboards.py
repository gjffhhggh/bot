from telebot import types
from bot import *

markupinline = types.InlineKeyboardMarkup(row_width=2)
keyboard1 = types.InlineKeyboardButton("VulnHub", callback_data='VulnHub1')
keyboard2 = types.InlineKeyboardButton("skipfish", callback_data='skipfish1')
keyboard3 = types.InlineKeyboardButton("sqlmap", callback_data='sqlmap1')
keyboard4 = types.InlineKeyboardButton("wpscan", callback_data='wpscan1')
keyboard5 = types.InlineKeyboardButton("cewl", callback_data='cewl1')
keyboard6 = types.InlineKeyboardButton("crunch", callback_data='crunch1')
keyboard7 = types.InlineKeyboardButton("hashcat", callback_data='hashcat1')
keyboard8 = types.InlineKeyboardButton("john", callback_data='john1')
keyboard9 = types.InlineKeyboardButton("medusa", callback_data='medusa1')
keyboard10 = types.InlineKeyboardButton("ncrack", callback_data='ncrack1')
keyboard11 = types.InlineKeyboardButton("ophcrack", callback_data='ophcrack1')
keyboard13 = types.InlineKeyboardButton("aircrack-ng", callback_data='aircrack')
keyboard14 = types.InlineKeyboardButton("fern wifi cracker", callback_data='fern')
keyboard15 = types.InlineKeyboardButton("kismet", callback_data='kismet1')
keyboard16 = types.InlineKeyboardButton("pixiewps", callback_data='pixiewps1')
keyboard17 = types.InlineKeyboardButton("reaver", callback_data='reaver1')
keyboard18 = types.InlineKeyboardButton("wifite", callback_data='wifite1')
keyboard19 = types.InlineKeyboardButton("clang", callback_data='clang1')
keyboard22 = types.InlineKeyboardButton("radare2", callback_data='radare')
keyboard23 = types.InlineKeyboardButton("metasploit framework", callback_data='metasploit')
keyboard24 = types.InlineKeyboardButton("msf payload creator", callback_data='msfpayloadcreator')
keyboard25 = types.InlineKeyboardButton("searchsploit", callback_data='searchsploit1')
keyboard26 = types.InlineKeyboardButton("social engineering toolkit", callback_data='social1engineeringtoolkit')
keyboard27 = types.InlineKeyboardButton("ettercap-graphical", callback_data='ettercapgraphical1')
keyboard28 = types.InlineKeyboardButton("macchanger", callback_data='macchanger1')
keyboard29 = types.InlineKeyboardButton("mitmproxy", callback_data='mitmproxy1')
keyboard30 = types.InlineKeyboardButton("netsniff-ng", callback_data='netsniffng1')
keyboard31 = types.InlineKeyboardButton("responder", callback_data='responder1')
keyboard32 = types.InlineKeyboardButton("wireshark", callback_data='wireshark1')
keyboard34 = types.InlineKeyboardButton("mimikatz", callback_data='mimikatz1')
keyboard35 = types.InlineKeyboardButton("powersploit", callback_data='powersploit1')
keyboard36 = types.InlineKeyboardButton("proxychains", callback_data='proxychains1')
keyboard37 = types.InlineKeyboardButton("weevely", callback_data='weevely1')
keyboard38 = types.InlineKeyboardButton("autopsy", callback_data='autopsy1')
keyboard39 = types.InlineKeyboardButton("binwalk", callback_data='binwalk1')
keyboard40 = types.InlineKeyboardButton("bulk_extractor", callback_data='bulk_extractor1')
keyboard41 = types.InlineKeyboardButton("hashdeep", callback_data='hashdeep1')
keyboard42 = types.InlineKeyboardButton("faraday IDE", callback_data='faraday')
keyboard43 = types.InlineKeyboardButton("maltego", callback_data='maltego1')





markupinline.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6,keyboard7, keyboard8, keyboard9, keyboard10, keyboard11,
	keyboard13, keyboard14, keyboard15, keyboard16, keyboard17, keyboard18, keyboard19,
	keyboard22, keyboard23, keyboard24, keyboard25, keyboard26, keyboard27, keyboard28, keyboard29, keyboard30, keyboard31,
	keyboard32, keyboard34, keyboard35, keyboard36, keyboard37, keyboard38, keyboard39, keyboard40, keyboard41,
	keyboard42, keyboard43)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'VulnHub1':
                bot.send_message(call.message.chat.id, 
                	'''VulnHub это сайт на котором вы можете найти много виртуальны машин с уязвимостями для оттачивания навыков взлома. Разной сложностей и на любой вкус.
					Сайт VulnHub - https://www.vulnhub.com/''')
            elif call.data == 'skipfish1':
                bot.send_message(call.message.chat.id, '''Skipfish — активный инструмент тестирования безопасности веб-приложений. 
				Он готовит интерактивную карту для целевого сайта, проводя рекурсивное сканирование. ... Окончательный отчет, созданный инструментом, призван служить основой для профессиональных оценок безопасности веб-приложений.''')
            elif call.data == 'sqlmap1':
                bot.send_message(call.message.chat.id, '''sqlmap — это инструмент с открытым исходным кодом для тестирования на 
                проникновение, который автоматизирует процесс выявления и эксплуатации уязвимости SQL-инъекця и захват серверов 
                баз данных. Он поставляется с мощным движком выявления и многими нишевыми функциями для конечного тестера на 
                проникновение, имеет широкий набор возможностей, начиная от сбора отпечатков баз данных по полученной от них 
                данным, до доступа к файловой системе и выполнения команд в операционной системе посредством внеполосных 
                (out-of-band) подключений.

                Официальный сайт - https://kali.tools/?p=816''')
            elif call.data == 'wpscan1':
                bot.send_message(call.message.chat.id, '''WPScan — это сканер уязвимостей WordPress, работающий по принципу 
				«чёрного ящика», т. е. без доступа к исходному коду. Он может быть использован для сканирования удалённых сайтов 
				WordPress в поисках проблем безопасности.

				Домашняя страница: http://wpscan.org/''')
            elif call.data == 'cewl1':
                bot.send_message(call.message.chat.id, '''CeWL - это приложение ruby, которое отслеживает заданный URL на 
                заданную глубину, по желанию следуя по внешним ссылкам, и возвращает список слов, которые затем можно использовать 
                для взломщиков паролей

                Сайт - https://digi.ninja/projects/cewl.php''')
            elif call.data == 'crunch1':
                bot.send_message(call.message.chat.id, 'Crunch — генератор словарей с паролями, в которых можно определить стандартную или заданную кодировку. Crunch может создать список слов со всевозможными комбинациями и перестановками в соответствии с заданными критериями. Данные, которые выводит crunch, могут быть отображены на экране, сохранены в файл или переданы в другую программу.')
            elif call.data == 'hashcat1':
                bot.send_message(call.message.chat.id, '''Hashcat — это самый быстрый в мире восстановитель (взломщик) паролей. 
				В настоящее время, Hashcat объединила в себе две ранее существовавшие отдельные ветки программы. Одна так и называлась Hashcat, а вторая называлась oclHashcat (а ещё раньше oclHashcat была разделена на собственно oclHashcat и cudaHashcat). В настоящее время абсолютно все версии слиты в одну, которая при восстановлении паролей использует центральный процессор и видеокарту.''')
            elif call.data == 'john1':
                bot.send_message(call.message.chat.id, '''John the Ripper создан быть многофункциональным и быстрым. Он совмещает 
                несколько режимов взлома в одной программе и полностью настраиваем под ваши конкретные нужды (вы даже можете 
                определить пользовательские режимы взлома используя встроенную поддержку компилятора подмножества C). Также John 
                доступен на нескольких разных платформах, что даёт вам возможность использовать одинаковый взломщик везде (вы даже 
                можете продолжить сессию взлома, которую вы начали на другой платформе).''')
            elif call.data == 'medusa1':
                bot.send_message(call.message.chat.id, '''Medusa — это быстрый, параллельный и модульный брут-форсер входа. Цель заключается в поддержке такого количество служб, на которых возможна удалённая аутентификация''')
            elif call.data == 'ncrack1':
                bot.send_message(call.message.chat.id, '''Patator – это многоцелевой брут-форсер, с модульным дизайном и гибким использованием.''')
            elif call.data == 'ophcrack1':
                bot.send_message(call.message.chat.id, '''Ophcrack - это бесплатная программа с открытым исходным кодом, которая взламывает пароли для входа в Windows, используя хэши LM через радужные таблицы. Программа включает в себя возможность импортировать хэши из различных форматов, включая дамп непосредственно из файлов SAM Windows''')
            elif call.data == 'aircrack':
                bot.send_message(call.message.chat.id, '''Aircrack-ng — это программа по взлому ключей 802.11 WEP и WPA/WPA2-PSK.''')
            elif call.data == 'fern':
                bot.send_message(call.message.chat.id, '''Fern Wifi Cracker — это программное обеспечение для аудита беспроводной безопасности, написано с использованием языка программирования Python и библиотеки Python Qt GUI. Программа способна взламывать и восстанавливать WEP/WPA/WPS ключи и также запускать другие сетевые атаки на беспроводные или проводные сети.''')
            elif call.data == 'kismet1':
                bot.send_message(call.message.chat.id, '''Kismet — это детектор беспроводных сетей 802.11, сниффер и система выявления вторжений. Kismet будет работать с любыми беспроводными картами, которые поддерживают сырой режим наблюдения и может сниффить трафик 802.11b, 802.11a, 802.11g и 802.11n (если позволяет аппаратная часть и драйверы).''')
            elif call.data == 'pixiewps1':
                bot.send_message(call.message.chat.id, '''Pixiewps — это инструмент, написанный на C, он используется для оффлайн брутфорса пина WPS посредством эксплуатирования низкой или несуществующий энтропии некоторых точек доступа (атака pixie dust). Он предназначен только для образовательных целей. Вся благодарность за исследования направляется Dominique Bongard.''')
            elif call.data == 'reaver1':
                bot.send_message(call.message.chat.id, '''Reaver предназначен для подборки пина WPS (Wifi Protected Setup) методом перебора. Reaver создан для надёжной и практичной атаки на WPS, он прошёл тестирование на большом количестве точек доступа с разными реализациями WPS. В среднем, Reaver раскрывает пароль WPA/WPA2 в виде простого текста целевой точки доступа (ТД) за 4-10 часов, в зависимости от ТД. На практике, ему обычно нужна половина этого времени на предположение пина WPS и разгадки пароля.''')
            elif call.data == 'wifite1':
                bot.send_message(call.message.chat.id, '''Wifite был создан для использования с дистрибутивами на тестирование на проникновение, такими как Kali Linux, Pentoo, BackBox; любыми дистрибутивами Linux с пропатченным для инжекта беспроводными драйверами. По видимому, также работает на Ubuntu, Debian и Fedora.''')
            elif call.data == 'clang1':
                bot.send_message(call.message.chat.id, '''Clang — это транслятор для C-подобных языков, созданный специально для работы на базе LLVM. Комбинация Clang и LLVM представляет собой полноценный компилятор и предоставляет набор инструментов, позволяющих полностью заменить GCC. Благодаря архитектуре, основанной на библиотеках, Clang (как и LLVM) легко встраивается в другие приложения.''')
            elif call.data == 'radare':
                bot.send_message(call.message.chat.id, '''Бесплатный набор инструментов для упрощения нескольких задач низкого уровня, таких как криминалистика, реверс-инжиниринг программного обеспечения, эксплуатация, отладка. Он состоит из нескольких библиотек (которые расширяются с помощью плагинов) и программ, которые можно автоматизировать практически с любым языком программирования.''')
            elif call.data == 'metasploit':
                bot.send_message(call.message.chat.id, '''Metasploit – это платформа для тестирования на проникновение, с которой вы можете находить, эксплуатировать и подтверждать уязвимости.
				Домашняя страница: https://www.metasploit.com/''')
            elif call.data == 'msfpayloadcreator':
                bot.send_message(call.message.chat.id, '''Быстрый способ сгенерировать различные «базовые» полезные нагрузки Meterpreter через msfvenom (часть платформы Metasploit).
				MSFvenom Payload Creator (MSFPC), создатель полезной нагрузки MSFvenom, - это обёртка для создания нескольких типов полезной нагрузки на основе выбора пользователя. Идея в том, чтобы упростить насколько возможно (требуется только один ввод) создание полезной нагрузки.''')
            elif call.data == 'searchsploit1':
                bot.send_message(call.message.chat.id, '''Официальный инструмент поиска по базе данных эксплойтов Exploit Database''')
            elif call.data == 'social1engineeringtoolkit':
                bot.send_message(call.message.chat.id, '''Social-Engineer Toolkit (набор для социальной инженерии) — это фреймворк с открытым исходным кодом для тестирования на проникновение, предназначен для социальной инженерии. SET имеет ряд векторов атак по запросу, которые позволяют вам быстро сделать правдоподобную атаку.''')
            elif call.data == 'ettercapgraphical1':
                bot.send_message(call.message.chat.id, '''Ettercap — это всеобъемлющий набор для атаки "человек посередине" (MitM). Он умеет сниффить (прослушивать) живые соединения, фильтровать на лету содержимое передаваемых данных и многие другие трюки. Он поддерживает активное и пассивное вскрытие многих протоколов и включает многие функции для анализа сети и хостов.''')
            elif call.data == 'macchanger1':
                bot.send_message(call.message.chat.id, '''MAC-адрес (ещё называют физический адрес) – это уникальный идентификатор сетевого интерфейса в локальной сети. Одно устройство (компьютер, роутер) может иметь несколько сетевых интерфейсов (проводных и беспроводных) и, следовательно, иметь несколько MAC-адресов.''')
            elif call.data == 'mitmproxy1':
                bot.send_message(call.message.chat.id, '''mitmproxy – это интерактивная консольная программа, которая позволяет перехватывать, инспектировать, модифицировать и повторно воспроизводить поток трафика.''')
            elif call.data == 'netsniffng1':
                bot.send_message(call.message.chat.id, '''Высокопроизводительный сетевой сниффер Linux для инспекции пакетов.''')
            elif call.data == 'responder1':
                bot.send_message(call.message.chat.id, '''Responder это инструмент для выполнения атаки человек-посередине в отношении методов аутентификации в Windows. Эта программа включает в себя травитель LLMNR, NBT-NS и MDNS благодаря которому перенаправляется трафик с запросами и хешами аутентификации. Также в программу встроены жульнические серверы аутентификации HTTP/SMB/MSSQL/FTP/LDAP, которые поддерживают такие методы аутентификации как NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP и базовую HTTP аутентификацию, для которых Responder выполняет роль ретранслятора.''')
            elif call.data == 'wireshark1':
                bot.send_message(call.message.chat.id, '''Wireshark — это самый первостепенный во всём мире анализатор сетевых протоколов. Он позволяет вам видеть на микроскопическом уровне что происходит в вашей сети. Де-факто (и часто де-юре) он стал стандартом во многих индустриях и образовательных учреждениях.''')
            elif call.data == 'mimikatz1':
                bot.send_message(call.message.chat.id, '''Небольшой инструмент, для игры с безопасностью Windows.''')
            elif call.data == 'powersploit1':
                bot.send_message(call.message.chat.id, '''PowerSploit – это коллекция модулей Microsoft PowerShell, которые могут использоваться в помощь тестерам на проникновение во время фазы оценки. PowerSploit состоит из следующих модулей и скриптов:''')
            elif call.data == 'proxychains1':
                bot.send_message(call.message.chat.id, '''ProxyChains – это UNIX программа, которая подцепляет связанные с сетью libc функции в ДИНАМИЧЕСКИ СВЯЗЫВАЕМЫХ программах через предварительно загруженный DLL (dlsym(), LD_PRELOAD) и перенаправляет подключения через SOCKS4a/5 или HTTP прокси.
				Она поддерживает только TCP (UDP/ICMP и т.д. отсутствует).
				Поддерживаемые платформы: Linux, BSD, Mac.''')
            elif call.data == 'weevely1':
                bot.send_message(call.message.chat.id, '''Weevely – это веб-шелл командной строки, динамически распространяемый по сети во время выполнения, предназначен для удалённого администрирования и тестирования на проникновение. Просто закиньте PHP скрипт, и программа обеспечит похожий на ssh терминал даже в ограниченном окружении.''')
            elif call.data == 'autopsy1':
                bot.send_message(call.message.chat.id, '''Autopsy — это платформа цифровой криминалистики и графический интерфейс для Sleuth Kit и других цифровых криминалистических инструментов. Она используется правоохранительными органами, военными и корпоративными экспертами для расследования происшедшего на компьютерах. Обычные пользователи могут использовать её, например, для восстановления фотографий с цифровой карты памяти камеры.''')
            elif call.data == 'binwalk1':
                bot.send_message(call.message.chat.id, '''Инструмент поиска в заданном бинарном образе включённых файлов.''')
            elif call.data == 'bulk_extractor1':
                bot.send_message(call.message.chat.id, '''Инструмент массового извлечения Email и URL.''')
            elif call.data == 'hashdeep1':
                bot.send_message(call.message.chat.id, '''hashdeep — это кроссплатформенный инструмент для вычисления хешей или дайджестов сообщений для любого числа файлов, поддерживает рекурсивный обход структуры директорий. Также может искать файлы по известным хешам, либо отображать файлы, которые не совпадают с введёнными хешами. Поддерживаются хеши MD5, SHA-1, SHA-256, Tiger и Whirlpool hashes.''')
            elif call.data == 'faraday':
                bot.send_message(call.message.chat.id, '''Faraday представляет новую концепцию — IPE (Integrated Penetration-Test Environment, т. е. интегрированная среда тестирования на проникновение), это многопользовательская IDE для тестов на проникновение. Предназначен для распространения, индексации и анализа данных, полученных во время аудита безопасности.
				Основная цель Faraday — это использование доступных инструментов в сообществе для получения преимуществ многопользовательского режима.''')
            elif call.data == 'maltego1':
                bot.send_message(call.message.chat.id, '''Maltego — это инструмент для построение и анализа связей между различными субъектами и объектами. Её особенностями являются: визуализирование полученных данных, разведка на основе открытых источников, комбинирование для глубокого анализа данных полученных из закрытых и открытых источников, автоматический анализ открытых источников и автоматическое построение взаимосвязей между обнаруженными объектами.''')
 
            

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Чтобы обратно открыть список, используйте команду /start",
                reply_markup=None)
 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Выбрана утилита!")
    except Exception as e:
        print(repr(e))