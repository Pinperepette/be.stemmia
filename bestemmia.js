var bestemmia_array = ['dio porco ', 'cristo la madonna ', 'madunassa ', 'gesù inchiodato sulla croce ', 'madonna puttanaccia ', 'dio culo infiammato ', 'dio can ', 'Ave Maria piena di Merda ', 'Dio, Madonna e tutti gli angeli in colonna ', 'Gesù scalzo in una valle di chiodi ', 'Gesù cieco in una valle di spigoli ', 'Porco Dio e Padre Pio ', 'Bastardo il clero ', 'Madonna cagna ', 'Dio cantante, Madonna musicante, Giuseppe batterista e Cristo in autopista ', 'Maria putrefatta ', 'Dio bastardo ', 'Madonna inculata da cristo, quel bastardo', 'Gesù scalzo sui vetri rotti ', 'Gesù cantalupo', 'Gesù coglioncello', 'Dio vongola', 'Dio alligatore', 'Gesù con la candida', 'Madonna storpia', 'Gesù impiegato INPS', 'Giuseppe trapezista vedovo con alzheimer']

function singola_bestemmia(){
	var randbestemmia = Math.floor((Math.random() * bestemmia_array.length) + 0);
	console.log(bestemmia_array[randbestemmia]);
};

function bestemmia(numero=1){
	for(var i=0; i<numero; i++)
		singola_bestemmia();
};

