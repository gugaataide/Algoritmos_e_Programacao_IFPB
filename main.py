tipodecarne = str(input()).upper()
precofinal = 0
if tipodecarne in "CBFBS":
  paodealho = str(input())
  bebidaadulto = str(input())
  bebidacrian = str(input())
  quantidadecrian = int(input())
  quantidadeadulto = int(input())
  if bebidacrian in "S":
    precobebidacrian =  3 * quantidadecrian
    precofinal += precobebidacrian
  if bebidaadulto in "S":
    precobebidaadulto = 16*quantidadeadulto
    precofinal += precobebidaadulto
  if tipodecarne in "C":
    kgbovinoadulto = 0.2 * quantidadeadulto
    kgfrangoadulto = 0.1 * quantidadeadulto
    kgsuinoadulto = 0.1 * quantidadeadulto
    precoadulto = (32 * kgbovinoadulto) + (18 * kgfrangoadulto) + (15 * kgsuinoadulto)
    kgbovinocrian = 0.2 * quantidadecrian
    precocrian = 32 * kgbovinocrian
    precofinal += precoadulto + precocrian

  elif tipodecarne in "BF":
    kgbovinoadulto = 0.25 *quantidadeadulto
    kgfrangoadulto = 0.15 * quantidadeadulto
    kgbovinocrian = 0.2 * quantidadecrian
    precoadulto = (32 * kgbovinoadulto) + (18*kgfrangoadulto)
    precocrian = 32 * kgbovinocrian
    precofinal += precocrian + precoadulto

  elif tipodecarne in "BS":
    kgbovinoadulto = 0.25 * quantidadeadulto
    kgsuinoadulto = 0.15 * quantidadeadulto
    kgbovinocrian = 0.2 * quantidadecrian
    precoadulto = (32 * kgbovinoadulto) + (15 * kgsuinoadulto)
    precocrian = (32 * kgbovinocrian)
    precofinal += precoadulto + precocrian


  if paodealho in "Nn":
    precofinal = precofinal*0.98



  print(f"R$: {precofinal:.2f}")



else:
  print("Opção inválida.")
