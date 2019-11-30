******
Arrays
******

Declaration
===========
``ARRAY=()`` Declares an indexed array ARRAY and initializes it to be empty. This can also be used to empty an existing array.

``ARRAY[0]=`` Generally sets the first element of an indexed array. If no array ARRAY existed before, it is created.

``declare -a ARRAY`` Declares an indexed array ARRAY. An existing array is not initialized.
``declare -A ARRAY`` Declares an associative array ARRAY. This is the one and only way to create associative arrays.

Storing values
==============
``ARRAY[N]=VALUE`` Sets the element N of the indexed array ARRAY to VALUE. N can be any valid arithmetic expression.

``ARRAY[STRING]=VALUE`` Sets the element indexed by STRING of the associative array ARRAY.

``ARRAY=VALUE`` As above. If no index is given, as a default the zeroth element is set to VALUE. Careful, this is even true of associative arrays - there is no error if no key is specified, and the value is assigned to string index "0".

``ARRAY=(E1 E2 ...)`` Compound array assignment - sets the whole array ARRAY to the given list of elements indexed sequentially starting at zero. The array is unset before assignment unless the ``+=`` operator is used. When the list is empty (``ARRAY=()``), the array will be set to an empty array. This method obviously does not use explicit indexes. An associative array can not be set like that! Clearing an associative array using ``ARRAY=()`` works.

``ARRAY=([X]=E1 [Y]=E2 ...)`` Compound assignment for indexed arrays with index-value pairs declared individually (here for example X and Y). X and Y are arithmetic expressions. This syntax can be combined with the above - elements declared without an explicitly specified index are assigned sequetially starting at either the last element with an explicit index, or zero.

``ARRAY=([S1]=E1 [S2]=E2 ...)`` Individual mass-setting for associative arrays. The named indexes (here: S1 and S2) are strings.

``ARRAY+=(E1 E2 …)`` Append to ARRAY.
``ARRAY=("${ANOTHER_ARRAY[@]}")`` Copy ANOTHER_ARRAY to ARRAY, copying each element.

Getting values
==============
``${ARRAY[N]}`` Expands to the value of the index N in the indexed array ARRAY. If N is a negative number, it's treated as the offset from the maximum assigned index (can't be used for assignment) - 1

``${ARRAY[S]}`` Expands to the value of the index S in the associative array ARRAY.

``"${ARRAY[@]}"``
``${ARRAY[@]}```
``"${ARRAY[*]}"``
``${ARRAY[*]}`` Similar to mass-expanding positional parameters, this expands to all elements. If unquoted, both subscripts * and @ expand to the same result, if quoted, @ expands to all elements individually quoted, * expands to all elements quoted as a whole.

``"${ARRAY[@]:N:M}"``
``${ARRAY[@]:N:M}``
``"${ARRAY[*]:N:M}"``
``${ARRAY[*]:N:M}`` Similar to what this syntax does for the characters of a single string when doing substring expansion, this expands to M elements starting with element N. This way you can mass-expand individual indexes. The rules for quoting and the subscripts * and @ are the same as above for the other mass-expansions.

Metadata
========
``${#ARRAY[N]}`` Expands to the length of an individual array member at index N (stringlength)

``${#ARRAY[STRING]}`` Expands to the length of an individual associative array member at index STRING (stringlength)

``${#ARRAY[@]}``
``${#ARRAY[*]}`` Expands to the number of elements in ARRAY

``${!ARRAY[@]}``
``${!ARRAY[*]}`` Expands to the indexes in ARRAY since BASH 3.0

Destruction
===========
``unset -v ARRAY``
``unset -v ARRAY[@]``
``unset -v ARRAY[*]`` Destroys a complete array
``unset -v ARRAY[N]`` Destroys the array element at index N
``unset -v ARRAY[STRING]`` Destroys the array element of the associative array at index STRING