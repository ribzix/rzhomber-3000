import random
import discord
from discord.ext import commands

###### ШУТКИ ######

beg = ["знаете в чем разница между говном и краковской колбасой? ","встретились как-то два деревенских дурочка ",
       "сидели две бабки на скамейке ","встречается испанец, русский и немец ","встретились как-то подводник, пилот и машенист ",
       "сижу пержу ","подошёл отец к сыну и пизданул его с локтя ","чайник, кружка ","поспорили как-то два еврея ",
       "вы когда нибудь задумываль над такой проблемой? ","помните когда в школе ","Фирма ищет нового бухгалтера ",
       "автобус, стоят все прижатые друг к другу настолько плотно, что аж интимно ","все думают, что мечта каждой девушки - найти идеального парня ",
       "купил очень скользкую клеёнку и постелил на кухонный стол ","если голый мужчина, случайно, попадает в женскую баню - женщины верещат и пытаются плеснуть на него кипятком ",
       "здравствуйте, дети! меня зовут Иван Васильевич, я ваш новый учитель русского языка и литературы ","девочка приходит из школы с фингалом ","летят в самолете американец, русский, француз, араб и еврей ",
       "пришел мужик к священнику и говорит ","проверяющий на одесском рынке ","cпекла бабка деду Колобок, но он получился какой-то неживой ","муж решил неожиданно навестить жену в командировке: ",
       "приходит бабка к врачу гинекологу и говорит ","забавная история: ","лижу я как-то член ","первая брачная ночь ","подходит Илья Муромец к грязной-прегрязной пещере и говорит: ",
       "в отличие от женщин, мужчины размножаются делением ","мужик возвращается домой раньше времени, заходит в квартиру и вдруг слышит из спальни голоса своего шефа и жены: ",
       "мужик просыпается утром, смотрит в окно, а у соседа во дворе огромный ","Девушка говорит парню: ",
       "у одного старого дедушки была жена - бабушка, которая лежала при смерти. пошел дедушка по врачам в надежде, что кто-нибудь поможет ему спасти бабушку, и в конце концов ",
       "после очередно рюмки водки дед спизданул: ","рассказал мне как-то хохол в маршрутке свою историю ","знаете, что говорил гитлер: ","как говорил сталин: ","после победы над гитлером все газеты писали: ",
       "Бык со львом пьют пиво. Льву на мобилу звонит жена. Лев отвечает: ","В России все болезни лечатся водкой:","У моего деда полно забавных историй: ","бывают в жизне такие моменты, когда хочется крикнуть: ",
       "Футбольный арбитр в спешке вместо карточки показал игроку презерватив. ","Разговаривают друзья: ","парень и девушка после бурной ночи, парень собирается уходить, и вдруг около выхода он видит фотографию мужчины. Он спрашивает: ",
       "если после двух холодных и дождливых дней потеплело, и светит яркое солнце - скорее всего ","зашел муж дома в туалет с мобильным в кармане, достает телефон, звонит на домашний - жена берет трубку. Жена: ",
       "вы знаете настоящую причину самоубийства гитлера: ","Отец мне говорил: "]

mid = ["у меня отвалился хер ","я смотрел на него он смотрел на мой член ","бывало? ",",а один и говорит 'я гей' ","после этого ","дело было непростое ","была непростая дилема ","в перестрелке погибло трое ",
       "водки мало ","повеселся на вешалке ","а отчим ему и говорит: ","он поедал рвотные массы ","он выдернул пробку из жопы ","эмэндэмс был сладковато-калого привкуса ","мне нассали в сменку ",
       "я блевал скителзом ","не помню когда проснулся помню что обоссался ","путин сосал у негра ","я поссал в фантан на день вдв ","я черпал кал галошей ","сижу с пальцем в жопе ","банка лопнула у меня в жопе ",
       "я нагнул её раком ","сарай распахнулся ","сиська бога ","я встал раком ","вернул его обратно ","так я подхватил спид ","въебал ему в пиздак ","заморил червячка ","я прошептал: ","всё таки забавно ",
       "в жизни все возможно ","попробывать кал ","хорошо жить не запретишь ","под пивко в рот заходит ","я выбрал синюю таблетку ","слушай внимательно щенок ","в трусах говно ","проснись, ты обосрался ",
       "ясен пенис что ","тупые школьники ","скажем так ","на фоне был флаг украины ","хуй упал в краску ","федералы не смогли это остановить "]

punch = ["иди нахуй ","я не ебу ","стояка нет ","мы начали трахать друг друга ","и так он стал петухом ","и так я оказался в тюрьме ",
         "делайте выводы ","а в конце всем отрезали пенисы ","всё таки тесно на земле ","грустно признавать, но это был я ","это был Энштейн ","иди поучись ",
         "на себя посмотри ","а я думал шляпа","ебаца хочется ","в конце негры надовали ему в рот ","арбуз был невкусным ","так я оказался в дагестане ","слон отдавил ему яйца ","в буфете продавали кал ",
         "сперма чебурашка ","сука бля","я петух ","после этого я порезал вены ","после этого меня сдали в детдом ","махнатая пизда ","сиськи до колена ","старый пидор ","а где блять ","я снял с себя шорты ",
         "грустно признавать, но это был путин ","и мы начали трахать его","забавно. на следующий день он умер ","так я стал инвалидом ","при сталине такой хуйни не было","рашка хули ","всё таки есть добрые люди на земле",
         "это была лужа кала ","это были мои лучшие воспоминания о детстве ","дед оказался прав ","мечты сбываются ","пососались и разошлись ","это было в украине, там все дебилы ","но никогда штирлец не был так близко к провалу",
         "все это пропагондировал навальный ","- это слоган ЛДПР "]

other = ["пердели старики ","дело было в казино ","один хохол послал его нахуй ","первый уточнил 'внатуре?'","переглядывались два инвалида ","подскочил хач ","тот возразил 'а может ты пидор?' ",
         "нет блять ","и тут я перданул ","возможно? ","проверенная схема ","везде было говно ","у инвалида стоял член ","у меня не стоит член ","дристал арбузом ","перданул и обосрал свои шорты ",
         "у меня нет отца ","секта калоедов ","тупое говно ","ты быдло ","пьяный хуй ","парашный дед ","соси мою боль ","сейчас сижу с вилкой в жопе ","дильфинья дырка ","жопоболь ","трахать тебя и всю твою семью "
         "тренер держал в руках член ","красный нос хуй в потолок врос ","во рту был кал ","помочился на памятник ленина ","так я стал петухом ","дрочибельно кста ","негры сбежали ","и шизов этих было двое ","дед оказался прав "
         "нихуёвая была пьянка ","отлепил трусы от жопы ","отчим оказал поддержу ","всё семейсво было в сборе ","богоугодная хуйня ","ламповая атмосфера ","вот они, корпаротивы "]

dia = ["представьте, однажды выяснилось, что государство выпускает кал ","папа я потерял таблетки! ","шеф, мне нужен отпуск!","Что-то больной вы мне не нравитесь... ","абрам, а как вы относитесь к построить синагогу в тюрьме?",
       "ага, еще и борщем облилась.","Папа, давай играть в Кощея Бессмертного?","попал ты мужик конкретно, рыбку то здесь нельзя ловить!","хорошая погодка ","при сталине было лучше ","сколько стоит свинина? ",
       "мать жива ","чекни мать ","увидимся в аду уёбок","я доем? ","ты тоже слушаешь стаса михайлова? ","Твой тоже курсы мудаков заканчивал? ","ты возле аэропорта? ","поможите мне с делемой? ","у меня негр в холодильнике ",
       "слово не воробей выпустишь - не застрелишь ","ах ты сукин сын, я в деле ","такого не планировалось ","ты уверен? ","фоткуют говно в еде ","хотел бы я встретить путина ","выпили с друзьями по таблетку слабительного"]

###### ПАСТЫ ######

pasta = ["«Нам насрать на низшие существа!» — раздался пронзительный голос со стороны параши. \n Но пацаны, как всегда, не обратили внимания на это визгливое кукареканье. Пусть кукарекает, что с него взять? \n Петух — не человек, и сегодня ему предстоит очень трудная ночь. У него уже в течение полутора лет каждая ночь была очень трудной, и теперь его анус был разработан настолько, что он без труда мог спрятать в нём банку сгущёнки.",
         "аноны тут такая тема произошла со мной. даже не знаю как сказать.. началось все в учебке- ко мне подошел один парень и предложил мне сделать минет бесплатно(он мне сделает). я отказался. парень был послан на хуй. на следующий день меня двое держали за волосы а третий провел членом по губам.\n мне сказали чтобы я сделал минет каждому, иначе они расскажут всем что было той ночью.\nкак быть аноны? осложняется все тем что один из них бодибилдер. выйгрывал чемпионат области по пауэрлифтингу. с легкостью меня взломал тогда.",
         "Cап, двач. История пойдет о моих школьных годах, когда я учился в классе илдак десятом. Был у нас в классе один додик по имени Слава, был он человеком действительно странным: ни с кем не общался,\nдоставал жвачку из под парты и жрал её как ебаный примат, при этом ковыряя в носу пальцем и смачно чавкая, на переменах постоянно пытался вздрочнуть в школьном толкане (воняло там как в газовой камере, хуй пойми как он это там делал),\nпосле школы он не шёл домой, а сидел на лавке и вдуплял в кирпичную стену школы пуская слюну. За неделю до летних каникул произошёл один случай: во время перемены была гробовая тишина, весь класс занимался своим повседневным \nдолбоебизмом и деградацией, как вдруг тишину прервал Слава. Совершенно нелюдимый и наглухо отбиты, он за всё время учебы и руки не поднял, подошёл к учителю, все обратили на это внимание и ждали что же он спизданёт.\n И тут Слава открывает свой грязный помойный рот, из котороко несло жвачками столетней давности и спрашивает 'Светлана Владимировна, сколько будет 150+150?'По лицу светланы владимировны было понятно, что она в ахуе от вопросад \nесятиклассника нахуй. Но после кратковременного ступора ответила: '300', после этого Слава сказал 'А я думал памперс' и начал истерично ржать как ёбнутый мешком. В таком состоянии он дошёл до своей парты и сел на место, в то время"]

###### РЭП ######

r_beg = ["Я лью Cristal и ","Летит в ночной Москве ","Трачу на это, трачу на ","Эти цепи на мне ","Заберу всё, будто бы я ","Поработай в постели ","Так проходит каждый ","В моём доме, как в отеле ","Им известно, мой карман ",
         "Детка, это всё не в счёт","Отец мне говорил: ","Ты отравляешь мой мозг, и всё это","Я кручу дерьмо прямо на ","Но она не любит игры, она любит ","Чем я заслужил внимание этих ","Я тот самый грязный заяц, но перед ними я ",
         "Знаю, что сука мне врёт, я до последней капли "]


###### CMD ######

class MyClient(discord.Client):
    async def on_read(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

###### КОМАНДЫ ######

TOKEN = "ODMyMTk1Nzk1MDQyMTcyOTY5.YHgQug.CFanWmHOIMi-TlcwJ7-2oKHx2oU"

bot = commands.Bot(command_prefix=('!'))
bot.remove_command( 'help' )

@bot.command()
async def шутка(ctx):
    joke_type = "аааааааааа"
    type = random.randint(0,4)
    if type == 0:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(other)+random.choice(punch)
    if type == 1:
        joke_type = random.choice(beg)+random.choice(mid)+"\n - "+random.choice(dia)+"\n - "+random.choice(dia)+"\n "+random.choice(punch)
    if type == 2:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(other)+random.choice(other)+random.choice(punch)
    if type == 3:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(mid)+random.choice(other)+random.choice(other)+random.choice(punch)
    if type == 4:
        joke_type = "иди нахуй"
    await ctx.send(joke_type)

@bot.command()
async def шутки(ctx):
    joke_type = "аааааааааа"
    type = random.randint(0,4)
    if type == 0:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(other)+random.choice(punch)
    if type == 1:
        joke_type = random.choice(beg)+random.choice(mid)+"\n - "+random.choice(dia)+"\n - "+random.choice(dia)+"\n "+random.choice(punch)
    if type == 2:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(other)+random.choice(other)+random.choice(punch)
    if type == 3:
        joke_type = random.choice(beg)+random.choice(mid)+random.choice(mid)+random.choice(other)+random.choice(other)+random.choice(punch)
    if type == 4:
        joke_type = "иди нахуй"
    await ctx.send(joke_type)

@bot.command()
async def паста(ctx):
    await ctx.send(random.choice(pasta))

@bot.command()
async def rbot(ctx):
    await ctx.send("Йоу, мудилы! У вас одна минута на вход в игру")
    emoji = '✅'
    message = await ctx.send
    await message.add_reaction(emoji)











###### КЛИЕНТ ######

client = MyClient()
bot.run(TOKEN)
