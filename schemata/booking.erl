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


        {field, [
            {name, "id"}, %% ie, the galileo number
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string} 
        ]},

        {field, [
            {name, "flights"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string} %% Again, a list, for example ['TG921', 'TG920']
        ]},

        {field, [
            {name, "passengers"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string} %% A list of passengers (with their randomly created id)
        ]},

        {field, [
            {name, "fares"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string} %% list of fares (random ids)
        ]},

        {dynamic_field, [
            {name, "*"}
        ]}
    ]
}.
