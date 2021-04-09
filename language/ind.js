const a = '```'

exports.wrongf = () => {
	return`*format salah/text kosong*`
}

exports.noregis = () => {
	return`*「 DATA REGISTER 」*\n\n*cara daftar ${prefix}daftar NAME|AGE* \n*contoh ${prefix}daftar Riu|17*`
}

exports.rediregis = () => {
	return`*「 SUDAH DAFTAR 」*\n\n*kamu sudah terdaftar di database bot*`
}

exports.registered = (namaUser, umurUser, serialUser, time, sender) => {
	return`*「 DATA REGISTERED SUCCESSFULLY 」*\n\nkamu sudah terdaftar dengan data \n\n┏━⊱NAME\n┗⊱${namaUser}\n┏━⊱NUMBER\n┗⊱wa.me/${sender.split("@")[0]}\n┏━⊱AGE\n┗⊱${umurUser}\n┏━⊱waktu pendaftaran\n┗⊱${time}\n\n┏━❉ *NS* ❉━\n┣⊱${serialUser}\n┗⊱NOTE : jangan sampai lupa nomer ini karena ini penting:v`
}
