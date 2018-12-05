es_instrumento(guitarra).
es_instrumento(bajo).
es_instrumento(organo).
es_instrumento(violin).
es_instrumento(tambor).
es_instrumento(platillos).
es_instrumento(contrabajo).

es_accesorio(correa).
es_accesorio(pedalera).
es_accesorio(porta_microfono).
es_accesorio(afinador).
es_accesorio(pegatina).
es_accesorio(amplificador).

es_repuesto(clavijero).
es_repuesto(cuerdas).
es_repuesto(parches).
es_repuesto(palillos).
es_repuesto(cables).

es_producto(name) :- es_repuesto(name);es_accesorio(name);es_instrumento(name).
es_alquilable(name) :- es_instrumento(name).
es_vendible(name) :- es_producto(name).
