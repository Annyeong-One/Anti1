from keep_alive import keep_alive
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('>help'):
		await message.channel.send(
		    '```안녕하세요, 봇 안티매터입니다.\n제 접두사는 >이에요.\n----------------------------------\n   가능한 명령어 목록\n> 와샌즈\n> 변\n> 멍청이\n> 안티매터\n> ?\n> dixdick\n> 변봇아도배해줘\n> 갸변저항\n> 오\n> 아\n> A```'
		)
	if message.content.startswith('>와샌즈'):
		await message.channel.send(
		    '언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다.'
		)
	if message.content.startswith('>변'):
		await message.channel.send('뭐 하는 거야!')
	if message.content.startswith('>멍청이'):
		await message.channel.send('그것은 바로 영빈이었네요!')
	if message.content.startswith('>안티매터'):
		await message.channel.send('https://ivark.github.io/')
	if message.content.startswith('>?'):
		await message.channel.send('.  ___  ')
		await message.channel.send('. |__ \ ')
		await message.channel.send('.     )  |')
		await message.channel.send('.   / / ')
		await message.channel.send('.  |_|  ')
		await message.channel.send('.  (_)  ')
	if message.content.startswith('>loop1'):
		await message.channel.send('>loop2')
	if message.content.startswith('>loop3'):
		await message.channel.send('>loop4')
	if message.content.startswith('>loop5'):
		await message.channel.send('>loop6')
	if message.content.startswith('>loop7'):
		await message.channel.send('>loop8')
	if message.content.startswith('>loop9'):
		await message.channel.send('>loop10')
	if message.content.startswith('>dixdick'):
		await message.channel.send('선사딕시대는 인류의 출현과 기원전 3000년경의 딕어의 문자인 원시 훈딕정음 등장 사이의 기간이다. 이때 현 신차난디아의 수도 워싱찬 딕.시. 부근에서는 딕클로투스족이 번성하여, 청동기 도구의 사용을 시작하였다. 당시에 열매 갸봉을 주식으로 하며 생활을 하던 딕클로투스족은 점차 지능이 떡상하게 되었고 그들만의 나라를 세우기 시작했다. 처음에는 딕클로투스들이 집단생활과 정착생활을 하기 시작했다.  그러자 자연스럽게 여러 다른 환경에서 적은한 딕클로투스 족들은 약 30여개의 다른 종으로 변했다.  그중 중요한 갸룬 민족, 영굴루레스족 , 딕킨족 등을 기억해두 면 좋겠다. 이들은 세력이 가장 센 세 종족이였다. 그리고 각 종족마다 족장이 생겨나기 시작했다. 그리고 나머지 단디룬족, 변바르족, 찌리리족 등 약 20여개의  세력이 약했던 종족들이 합쳐져 브레이누스 족이 탄생했다. 딕클로투스족의 신찬신 영접은 약 기원전 27년경에 일어났다. 이는 워싱찬 근처 산인 남산 디키즈 동굴의 Dix Dick 벽화에서 볼 수 있는데, 해당 벽화에는 신찬신이 약 30명의 인간 앞에서 하늘에서 내려오는 것을 볼 수 있다. 이들 중에는 갸룬 민족의 족장으로 보이는 인물과 브레이누스 족의 사람들, 그리고 벽화를 그린 종족으로 추정되는 영굴루레스족의 족장이 있다. 특이점으로는 이 그림의 배경에 매우 작은 비행하는 곤충이 그려져 있다는 것인데, 역사학자들의 연구에 따르면 이 벌레의 밑에 벌레가 소변을 누고 있는 그림을 지운 흔적이 있다고 한다. 신찬신의 영접 후에 언제 떠났는지 혹은 돌아왔는지에 대한 자료는 아직 없으나, 현재의 정설은 신찬신 영접 후 매우 짧은 시간 내에 신찬신이 없어졌다는 것이다. 이 사건 이후 각각의 종족에게는 종교까지 생겼는데 실질적으로는 이름만 다를뿐이지 같은 신찬신을 숭배하고 있는 것과 다름이 없었다. 현 신찬딕 역사학개론의 전문가들이 이 선사 딕 시대의 종교에 대하여 조사를 진행하고 있는중이다. 각 종족의 족장들은 글이 없었던 시대임에도 불구하고 자신들만의 규칙을 만들기 시작했다. 이것을 통하여 전 딕클로투스족 보다 훨씬 뛰어난 지능을 가진 것을 추측해볼 수 있다.')
		await message.channel.send('https://classroom.google.com/c/MjM2NTUyMDM1NTA2?cjc=oefkrbt')
	if message.content.startswith('>변봇아도배해줘'):
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
		await message.channel.send('오예')
	if message.content.startswith('>도움말'):
		await message.channel.send('도움말은 영레한테 쓰는 명령어라고요!\n```마음이 아플때 쓰는 접두사는 ^이에요.\n마음이 아플 때 쓰는 명령어\n> 영레\n> 너지금뭐하는거야\n> 영레새끼\n> 영빈아조용히해\n> 국어B\n> mhi의해구하기\n> 팔씨름하자 \n> 나는영레친구\n> 방광\n> ???(이스터에그 찾아보세요!)```')
	if message.content.startswith('>아'):
		await message.channel.send('그렇네!')
	if message.content.startswith('>오'):
		await message.channel.send('예!')
	if message.content.startswith('>갸변저항'):
		await message.channel.send('sd-ByunByunByun https://cdn.discordapp.com/attachments/805963165229776951/810504184163205180/SPOILER_bbbyyyuuunnn_-_Patricia_Taxxon_X_GyaByun_Resistor.mp3\n\n Aleph-Byun https://cdn.discordapp.com/attachments/805963165229776951/810504173858324480/SPOILER_Byun_-_LeaF__Optie__GyaByun_Resistor.mp3\n\n R https://cdn.discordapp.com/attachments/805963165229776951/810504149509996575/SPOILER_R_-_Plum_X_GyaByun_Resistor.mp3\n\n Byuntapper https://cdn.discordapp.com/attachments/805963165229776951/810504191591579658/SPOILER_byuntapper.mp3')
	if message.content.startswith('>A'):
		await message.channel.send('???: 아 얘들아 A형을 누가 90점을 못 맞니\n¿¿¿: 마음이 아프다')
	if message.content.startswith('>변목길이50킬로미터'):
		await message.channel.send('아아... 길이를 측정할 수 없을 만큼 깁니다... 뭐 대충 한 그 뭐냐 50km정도 되지 않을까요')


keep_alive()
client.run(os.getenv('TOKEN'))
