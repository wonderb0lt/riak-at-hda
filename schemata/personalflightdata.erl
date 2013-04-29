{
    schema,
    [
        {version, "1.2"},
        %%{default_field, "title"},
        {default_op, "or"},
        {n_val, 3},
        {analyzer_factory, {erlang, text_analyzers, whitespace_analyzer_factory}}
    ],
    [
        %% ID = $bookingid_$flightid?! 

        {field, [
            %% flight id to reservation detail (maybe also containing for whom the reservation is)
            {name, "seats"}, 
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string} %% JSON dictionary.
        ]},

        {field, [
            {name, "eTicket"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},


        {field, [
            {name, "seat"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
            {type, string}
        ]},


        {field, [
            {name, "services"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string} %% list of strings
        ]},

        {field, [
            {name, "baggage"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "class"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]}

        {field, [
            {name, "passengers"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string} %% A list of passengers (with their randomly created id)
        ]},
        %% A dynamic field. Catches any remaining fields in the
        %% document, and uses the analyzer_factory setting defined
        %% above for the schema.
        {dynamic_field, [
            {name, "*"}
        ]}
    ]
}.      