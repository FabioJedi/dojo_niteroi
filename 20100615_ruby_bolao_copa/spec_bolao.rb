require 'rubygems'
require 'spec'
require 'bolao'

describe 'bolao' do

  it 'deve retornar 0 pontos quando toda aposta estiver errada' do
    aposta = Resultado.new(0, 0)
    resultado_final = Resultado.new(2, 1)
    aposta.pontuacao_resultado(resultado).should == 0
  end

  it '"Mario" nao acerta nada' do
    apostador1 = "Mario"
    bolao(apostador1, "0x0", "2x1").should == [apostador1, 0]
  end

  it '"Mario" acerta um resultado' do
    apostador1 = "Mario"
    bolao(apostador1, "0x1", "2x1").should == [apostador1, 1]
  end

end
