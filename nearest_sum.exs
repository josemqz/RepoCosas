defmodule NearestSum do

	# obtener elemento más cercano a (value - l) en lista ordenada
	def bin_search(l, sort_list, value, izq, der, med) do

		actValue = value - l
		med = 
			if med != 0 && med != (length(sort_list) - 1) do
				div((der + izq), 2)
			else
				med
			end
			
		medItem = Enum.at(sort_list, med)
		#IO.inspect {izq, der, med, medItem, actValue}, label: "izq, der, med, mi, actValue"

		{item, diff} =
			cond do
			
			# par exacto
			medItem == actValue ->
				#IO.inspect medItem, label: "item encontrado, diff: 0"
				{medItem, 0}

			# final de búsqueda
			(der - izq) < 1 ->
				#IO.puts "\nfinal búsqueda"

				diff1 = abs(medItem - actValue)

				#comparar con vecino para saber cuál es el más cercano
				delta = 
					cond do
					medItem < actValue and med != (length(sort_list) - 1) ->
						#IO.puts "actValue es mayor"
						1  # elemento siguiente

					medItem > actValue and med != 0 ->
						#IO.puts "actValue es menor"
						-1 # elemento anterior

					true ->
							0
					end

				diff2 = abs(Enum.at(sort_list, med + delta) - actValue)

				if diff1 < diff2 do
					#IO.inspect {medItem, diff1, diff2}, label: "item encontrado, diff1, diff2"
					{medItem, diff1}
				else
					#IO.inspect {Enum.at(sort_list, (med+delta)), diff2, diff1}, label: "item encontrado, diff2, diff1"
					{Enum.at(sort_list, med + delta), diff2}
				end

			# búsqueda en segunda mitad
			medItem < actValue ->

				# borde superior
				izq =
					if med == (length(sort_list) - 1) do
						#IO.puts "borde superior"
						der
							
					else
						#IO.puts "segunda mitad"
						med + 1
					end
				
				med = div( (der + izq), 2)

				bin_search(l, sort_list, value, izq, der, med)

			# búsqueda en primera mitad
			true ->

				# borde inferior
				der =
					if med == 0 || med == izq do
						#IO.puts "borde inferior"
						izq

					else
						#IO.puts "primera mitad"
						med - 1
					end

				med = div( (der + izq), 2)
				
				bin_search(l, sort_list, value, izq, der, med)
			end

			{item, diff}
	end


	# recorrer lista recursivamente
	def eachList([l | tail], sort_list, izq, der, med, value, item_1, item_2, min_diff) do
		
		#IO.inspect l, label: "\nl actual"

		{act_item, diff} = bin_search(l, sort_list, value, izq, der, med)

		#IO.inspect act_item, label: "act_item"
		{item_1, item_2, min_diff} = 

			cond do
			diff == 0 ->
				IO.puts "\npar exacto!"
				{l, act_item, diff}

			diff < min_diff ->
				#IO.inspect {diff}, label: "nuevo min_diff (menor diferencia)"
				{l, act_item, diff}

			true ->
				{item_1, item_2, min_diff}
			end
		
		eachList(tail, sort_list, izq, der, med, value, item_1, item_2, min_diff)
	end

	# final de recursión
	def eachList([], _, _, _, _, _, item_1, item_2, _) do
		{item_1, item_2}
	end


	# ordenar lista más larga y recorrer lista más corta
	def sortAndStart(list_to_sort, short_list, value) do
	
		min_diff = 999999
		item_1 = -999999
		item_2 = -999999

		# merge sort ;)
		list_to_sort = Enum.sort(list_to_sort)

		izq = 0
		der = length(list_to_sort) - 1
		med = div( (der + izq), 2)

		{item_1, item_2} =
			eachList(short_list, list_to_sort, izq, der, med, value, item_1, item_2, min_diff)

		{item_1, item_2}
	end


	# obtener elementos de list_1 y list_2 cuya suma esté más cercana a value
	def get_nearest_sum(list_1, list_2, value) do

		{item_1, item_2} = 

			# ordenar lista más grande
			if length(list_1) < length(list_2) do

				sortAndStart(list_2, list_1, value)

			else

				{item_1, item_2} = sortAndStart(list_1, list_2, value)
				{item_2, item_1}
			end

			{item_1, item_2}
	end
end


### TESTING

"""
list_1 = [24, 29, 9, 4, 21, 13, -2, 9, 10, 20]
# [-2, 4, 9, 9, 10, 13, 20, 21, 24, 29] -> 9 -> med = 5
list_2 = [10, 16, -3]
value = 23

{it1, it2} = NearestSum.get_nearest_sum(list_1, list_2,value)

IO.inspect {it1, it2}, label: "item_1, item_2"
IO.puts ""


list_1 = [7, 6, 10, -1]
list_2 = [8, 10, 29, 12]
value = 19

{it1, it2} = NearestSum.get_nearest_sum(list_1, list_2,value)

IO.inspect {it1, it2}, label: "item_1, item_2"
IO.puts ""


list_1 = [8, 13, 19, 24, 30]
list_2 = [20, 7, 28, 0]
value = 22

{it1, it2} = NearestSum.get_nearest_sum(list_1, list_2,value)

IO.inspect {it1, it2}, label: "item_1, item_2"
"""