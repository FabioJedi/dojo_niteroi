class Jogada

  @bola_da_vez
  @bola_alvo
  @acertou
  @matou

  def initialize(bola_da_vez, bola_alvo, acertou, matou)
    @bola_da_vez = bola_da_vez
    @bola_alvo = bola_alvo
    @acertou = acertou
    @matou = matou
  end

  def pontos
    if acertou
      @pontos = 0
    else
      @pontos = -1
    end
  end


end
