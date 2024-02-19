// Classe representando um herói de aventura
class Heroi {
    // Construtor da classe
    constructor(nome, idade, tipo) {
        this.nome = nome; // Propriedade nome
        this.idade = idade; // Propriedade idade
        this.tipo = tipo; // Propriedade tipo
    }

    // Método para o herói atacar
    atacar() {
        // Mensagem de ataque conforme o tipo do herói
        let ataque;
        switch (this.tipo) {
            case 'mago':
                ataque = 'usou magia';
                break;
            case 'guerreiro':
                ataque = 'usou espada';
                break;
            case 'monge':
                ataque = 'usou artes marciais';
                break;
            case 'ninja':
                ataque = 'usou shuriken';
                break;
            default:
                ataque = 'usou seus punhos';
        }

        // Exibir mensagem de ataque
        console.log(`O ${this.tipo} ${ataque}`);
    }
}

// Criar um herói
const meuHeroi = new Heroi('Lancelot', 30, 'guerreiro');

// Atacar com o herói
meuHeroi.atacar();
