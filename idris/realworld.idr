module hit

data person = Emily | McKenzie | Jimmy

hits: person -> person
hits Emily = McKenzie
hits McKenzie = Jimmy
hits Jimmy = Jimmy
