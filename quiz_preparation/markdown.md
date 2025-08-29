<!-- <h1>Heading level 1</h1> -->

<!-- # Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
#### Heading level 5
##### Heading level 6 -->

<!-- Heading level 1
===============
Heading level 1
= -->

<!-- Heading level 2
-----------

Heading level 2
- -->

<!-- Heading level 2
%%%%%%%%%%%%%%%%%% --> doesn't work like heading


______________________
______________________
Without blank lines, this might not look right.
# Heading
Don't do this!

______________________
______________________


This is the first line.  
And this is the second line.

First line with two spaces after.  
And the next line.

First line with the HTML tag after.<br>
And the next line.

I just love **bold text**.

I just love __bold text__.

Love **is** bold

*Love is* Italic

_Love is_ Italic

* one
* two
* three
* four

This text is ***really important***.

This text is ___really important___.

This text is __*really important*__.

This text is **_really important_**.

This text is **_really important_**.

<!-- bad practice -->
This is really ___very___ important text.

### Blackquote 1
> Dorothy followed her through many of the beautiful rooms in her castle.

> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### Blackquote 2
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### Blackquote 3 Nested
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

## Ordered List
4. First item
3. Second item
2. Third item
    1. First
    4. Second
4. Fourth item

## Unordered Lists

- First item
- Second item
- Third item
- Fourth item

* First item
* Second item

+ I
+ B


<!-- see difference with using without backslash -->
- 1968\. A great year! 

## code

        <html>
          <head>
            <title>Test</title>
          </head>

At the command prompt, type `nano`.

``Use `code` in your Markdown file.``

    <html>
      <head>
      <title>Ibad</title>
      </head>
    </html>

## Horizontal Rules

***
***
___

Four

---

___

<!-- Horizontal Rule Best Practices
For compatibility, put blank lines before and after horizontal rules -->

## Simple Link

[Duck Duck Go](https://duckduckgo.com)

## Link with tool tip

[Duck Duck Go](https://duckduckgo.com "The best search engine for privacy")

## Auto Link (URL / Email)

<https://www.markdownguide.org>

<fake@example.com>

## Formatting Links

I love supporting the **[Eff](https://eff.org)**.

This is the *[Markdown Guide](https://www.markdownguide.org)*.

See the section on [`code`](#code).

## Reference-style Link

In a hole in the ground there lived a [hobbit-hole][1], and that means comfort.

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"


# Images

* It open the image in new tab

[The San Juan Mountains are beautiful!](/mountains.avif "San Juan Mountains")

- It shows the image

![The San Juan Mountains are beautiful!](/mountains.avif "San Juan Mountains")

+ Image with Link

[![An old rock in the desert](/shiprock.avif "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

# Escaping Characters

\* Without the backslash, this would be a bullet in an unordered list.

\\d \`d`